import torch
from transformers import BertTokenizer, BertModel

from utills.SentenceUtill import SentenceUtill
from utills.StopWordUtill import StopWordsUtill
from utills.VectorUtill import VectorUtill

'''
    This class represent the bert model for the word embedding, and all the transformation stuff happens here
    Make sure the transform is installed
    Guide: https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/#word-vectors
'''
class BertProcessor:

    def __init__(self):

        # Load pre-trained model tokenizer (vocabulary)
        self._tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self._tokenConverter = BertTokenizer.from_pretrained('bert-base-uncased')

        # Load pre-trained model (weights)
        self._model = BertModel.from_pretrained('bert-base-uncased',output_hidden_states = True)
        # Put the model in "evaluation" mode, meaning feed-forward operation.
        self._model.eval()

        # sentence utils for extracting the sentences from the paragraph
        self._SENTENCE_UTIL = SentenceUtill()
        # stopwords utils to remove stop words on each sentence
        # will do the sentence processing prior to utilizing this util
        self._STOP_WORD_UTILL = StopWordsUtill()

        ## vector utils
        self._VECTOR_UTILL = VectorUtill()


        ## word vector list
        self._wordVectorListByBatch = []

    def getWordVectorListByBatch(self):
        return self._wordVectorListByBatch

    '''
        This method will initiate the process: extract sentences, performs tokenizations, BERT evaluations, returns
        list of word vectors extracted from the BERT
    '''
    def process(self, paragraph):
        if len(paragraph) == 0:
            return []

        ## extract the sentences
        sentenceList = self._SENTENCE_UTIL.extractSentencesFromParagraph(paragraph)

        ## tokens (MIGHT WE REMOVE THIS)
        ## tokens = self._removeStopWordsAndTokenizeSentences(sentenceList)

        ## builds tokens for the sentences and get the input ids
        inputIdList = self._processTokenization(sentenceList)

        ## sentence ids for each sentences
        segmentIdList = self._buildSegmentIdList(len(inputIdList),len(inputIdList[0]))

        # Convert inputs to PyTorch tensors
        tokensTensor = torch.tensor(inputIdList)
        segmentsTensors = torch.tensor(segmentIdList)

        # process with BERT
        hiddenStatesWithBatches = self._processBert(tokensTensor, segmentsTensors)

        # obtain word vectors by batches (sentences)
        self._extractWordVectorsByBatches(hiddenStatesWithBatches, inputIdList)


    '''This method will extract word vectors by sentences (batches)'''
    def _extractWordVectorsByBatches(self, hiddenStatesWithBatches, inputIdList):

        totalNumberOfBatches = len(inputIdList)
        batchIndex = 0

        while batchIndex < totalNumberOfBatches:
            currentBatchHiddenStates = []
            hiddenStateIndex = 0
            print("BertProcessor._extractWordVectorsByBatches >> Processing Batch : ", batchIndex)
            while hiddenStateIndex < len(hiddenStatesWithBatches):
                currentBatchHiddenStates.append(hiddenStatesWithBatches[hiddenStateIndex][batchIndex])
                hiddenStateIndex = hiddenStateIndex + 1

            ## compute vectors for current batch
            self._computeWordVectorsForBatch(currentBatchHiddenStates, batchIndex, inputIdList)
            batchIndex = batchIndex + 1

    '''This method computers word vectors for given batch'''
    def _computeWordVectorsForBatch(self, currentBatchHiddenStates, batchIndex, inputIdList):

        # Concatenate the tensors for all layers. We use `stack` here to
        # create a new dimension in the tensor.
        tokenEmbeddings = torch.stack(currentBatchHiddenStates, dim=0)
        # Remove dimension 1, the "batches".
        tokenEmbeddings = torch.squeeze(tokenEmbeddings, dim=1)
        # Swap dimensions 0 and 1.
        tokenEmbeddings = tokenEmbeddings.permute(1,0,2)

        tokenVectorSum = []
        # `token_embeddings` is a [22 x 12 x 768] tensor.
        # For each token in the sentence...
        for token in tokenEmbeddings:
            # `token` is a [12 x 768] tensor
            # Sum the vectors from the last four layers.
            sum_vec = torch.sum(token[-4:], dim=0)
            # Use `sum_vec` to represent `token`.
            tokenVectorSum.append(sum_vec)

        ## convert inputIds for current batch to tokens
        currentBatchTokens = self._tokenConverter.convert_ids_to_tokens(inputIdList[batchIndex])
        print("BertProcessor._computeWordVectorsForBatch >> Input Ids for current batch : ", inputIdList[batchIndex])
        print("BertProcessor._computeWordVectorsForBatch >> Tokens for current batch : ", currentBatchTokens)
        ## build word vector map
        currentBatchWordVectorMap = self._buildWordVectorMapForBatch(currentBatchTokens, inputIdList[batchIndex], batchIndex, tokenVectorSum)

        ## append to the main list
        self._wordVectorListByBatch.append(currentBatchWordVectorMap)
        ## START FROM HERE!!

    ''' This method builds word vector map for current batch'''
    def _buildWordVectorMapForBatch(self, currentBatchTokens, inputIdList, batchIndex, tokenVectorSum):

        index = 0
        currentWordIdList = []
        currentWordTokenList = []
        wordVectorMap = {}

        while index < len(currentBatchTokens):
            currentToken = currentBatchTokens[index]
            currentId = inputIdList[index]
            if self._isItCurrentTokenIsFragmentOfAWord(currentToken):
                ## keep adding the token and id
                currentWordIdList.append(inputIdList[index])
                currentWordTokenList.append(currentId)
            else:

                self._computeWordVectorAndExtractWordFromFragments(currentWordIdList, currentWordTokenList,
                                                                   tokenVectorSum, wordVectorMap)
                ## clear and store the currentId and currentToken
                currentWordIdList = [currentId]
                currentWordTokenList = [currentToken]

            ## increament the index
            index = index + 1

        ## incase if there is any left over
        if len(currentWordIdList) > 0 and len(currentWordTokenList) > 0:
            self._computeWordVectorAndExtractWordFromFragments(currentWordIdList, currentWordTokenList,
                                                               tokenVectorSum, wordVectorMap)

        return wordVectorMap

    ''' This method builds word vector map for current batch'''
    def _buildWordVectorMapForBatch2(self, currentBatchTokens, inputIdList, batchIndex, tokenVectorSum):
        index = 0
        currentWordIdList = []
        currentWordTokenList = []
        wordVectorMap = {}
        pass


    '''
        This method will group fragments of the word.
        ex: wa, ##t, ##ks, walter, bus, ##s ->> [ [wa, ##t, ##ks], [walter], [bus, ##s] ]
    '''
    def _groupWordFragments(self, currentBatchTokens, inputIdList):

        wordFragmentList = []
        currentTokenList = []
        index = 0
        ## remove all default tokens
        currentBatchTokens = self._removeDefaultTokens(currentBatchTokens)
        print("BertProcessor._groupWordFragments >> After removing the default tokens ", currentBatchTokens)
        while index < len(currentBatchTokens):
            currentToken = currentBatchTokens[index]
            currentTokenList.append(currentToken)
            ## traverse subsequent list to check for fragments
            index = index + 1
            fragmentEnded = False
            while fragmentEnded == False and index < len(currentBatchTokens):
                if self._isItCurrentTokenIsFragmentOfAWord(currentBatchTokens[index]):
                    ## keep adding
                    currentTokenList.append(currentBatchTokens[index])
                    index = index + 1
                else:
                    ## not a fragment any more
                    ## push the current Tokens list to the wordFragmentList
                    wordFragmentList.append(currentTokenList)
                    currentTokenList = []
                    fragmentEnded = True
        print("BertProcessor._groupWordFragments >> Grouped Fragments", wordFragmentList)
        return wordFragmentList

    '''
        This method computes word vectors for word, if the words are seperated by fragments
        it will sum up the vector values for all the fragments, and it will merge the fragments
        into single word
    '''
    def _computeWordVectorAndExtractWordFromFragments(self, currentWordIdList, currentWordTokenList, tokenVectorSum, wordVectorMap):
        if len(currentWordIdList) == 0:
            return

        # compute word vector and remove the #'s
        vectorsForTokens = []
        for index in range(len(currentWordTokenList)):
            ## first five values of the vector
            currentToken = str(currentWordTokenList[index])
            vectorsForTokens.append(tokenVectorSum[index][:5])

    ## summ all vectors
        vectorSum = vectorsForTokens[0].tolist()
        index = 1
        while index < len(vectorsForTokens):
            vectorSum = self._VECTOR_UTILL.addMatrixOfEqualSize(vectorSum, vectorsForTokens[index].tolist())
            index = index + 1

            ## remove #'s
        word = ""

        for token in currentWordTokenList:
            word = word + token.replace('#', '')

        ## append the word to the map
        wordVectorMap[word] = list(vectorSum)

    def _isItCurrentTokenIsFragmentOfAWord(self, token:str):
        return "#" in token

    '''This method process sentence with BERT, and returns the hidden states which will be used to computer word vectors'''
    def _processBert(self, tokensTensor, segmentsTensors):
        print("BertProcessor._processBert >> About evaluate sentences.")
        with torch.no_grad():
            outputs = self._model(tokensTensor, segmentsTensors)

            # Evaluating the model will return a different number of objects based on
            hiddenStatesWithBatches = outputs[2]
        print("BertProcessor._processBert >> Evaluated, and total of", len(hiddenStatesWithBatches[0]), "batches found.")
        return hiddenStatesWithBatches

    '''This method builds segment ids for each sentence'''
    def _buildSegmentIdList(self, numberOfSentences, lengthOfTokenArray):
        if numberOfSentences == 0 or lengthOfTokenArray == 0:
            return []
        sentenceIdList = []
        sentenceIndex = 0

        while sentenceIndex < numberOfSentences:
            sentenceIdList.append([sentenceIndex] * lengthOfTokenArray)
            sentenceIndex = sentenceIndex + 1
        print("BertProcessor._buildSegmentIdList >> Sentence Id list are built")
        return sentenceIdList

    '''This method tokenizes the sentences list, and returns inputs id list'''
    def _processTokenization(self, sentenceList):
        if len(sentenceList) == 0:
            return []
        print("BertProcessor._processTokenization >> Tokenization begins.")
        ## bert tokenizer takes sentenceList as an argument and add padding options as well
        bertTokenizer = self._tokenizer(sentenceList, padding=True)
        print("BertProcessor._processTokenization >> Tokenization ends.")
        return bertTokenizer["input_ids"]


    def _removeStopWordsAndTokenizeSentences(self, sentenceList):
        if len(sentenceList) == 0:
            return []

        sentenceListIndex = 0
        tokens = []

        while sentenceListIndex < len(sentenceList):
            ## remove stop words from the sentence
            currentSentence = self._STOP_WORD_UTILL.removeStopWords(sentenceList[sentenceListIndex])
            tokens.append(self._tokenizer.tokenize(currentSentence))
            sentenceListIndex = sentenceListIndex + 1
        return tokens

    def _removeDefaultTokens(self, currentBatchTokens):
        return list(filter(lambda x: (x != "[CLS]" and x != "[SEP]" and x != "[PAD]"), currentBatchTokens))



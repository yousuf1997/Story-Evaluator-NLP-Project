import torch
from transformers import BertTokenizer, BertModel

from utills.SentenceUtill import SentenceUtill
from utills.StopWordUtill import StopWordsUtill

'''
    This class represent the bert model for the word embedding, and all the transformation stuff happens here
    Make sure the transform is installed
    Guide: https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/#word-vectors
'''
class BertProcessor:

    def __init__(self):

        # Load pre-trained model tokenizer (vocabulary)
        self._tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

        # Load pre-trained model (weights)
        self._model = BertModel.from_pretrained('bert-base-uncased',output_hidden_states = True)
        # Put the model in "evaluation" mode, meaning feed-forward operation.
        self._model.eval()

        # sentence utils for extracting the sentences from the paragraph
        self._SENTENCE_UTIL = SentenceUtill()
        # stopwords utils to remove stop words on each sentence
        # will do the sentence processing prior to utilizing this util
        self._STOP_WORD_UTILL = StopWordsUtill()
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
        segmentIdList = self._buildSegmentIdList(len(inputIdList))

        # Convert inputs to PyTorch tensors
        tokensTensor = torch.tensor(inputIdList)
        segmentsTensors = torch.tensor(segmentIdList)

        # process with BERT
        hiddenStatesWithBatches = self._processBert(tokensTensor, segmentsTensors)

        # obtain word vectors by batches (sentences)
        self._extractWordVectorsByBatches(hiddenStatesWithBatches)


    '''This method will extract word vectors by sentences (batches)'''
    def _extractWordVectorsByBatches(self, hiddenStatesWithBatches):

        totalNumberOfBatches = len(hiddenStatesWithBatches[0])
        batchIndex = 0

        while batchIndex < totalNumberOfBatches:
            currentBatchTokens = []
            hiddenStateIndex = 0

            while hiddenStateIndex < len(hiddenStatesWithBatches):
                currentBatchTokens.append(hiddenStatesWithBatches[batchIndex])
                hiddenStateIndex = hiddenStateIndex + 1

            ## compute vectors for current batch
            self._computeWordVectorsForBatch(currentBatchTokens, batchIndex)

            batchIndex = batchIndex + 1

    '''This method computers word vectors for given batch'''
    def _computeWordVectorsForBatch(self, currentBatchTokens, batchIndex):

        # Concatenate the tensors for all layers. We use `stack` here to
        # create a new dimension in the tensor.
        tokenEmbeddings = torch.stack(currentBatchTokens, dim=0)
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
            print("Length is ", len(token))
            sum_vec = torch.sum(token[-4:], dim=0)
            # Use `sum_vec` to represent `token`.
            tokenVectorSum.append(sum_vec)
        ## START FROM HERE!

    '''This method process sentence with BERT, and returns the hidden states which will be used to computer word vectors'''
    def _processBert(self, tokensTensor, segmentsTensors):

        with torch.no_grad():
            outputs = self._model(tokensTensor, segmentsTensors)

            # Evaluating the model will return a different number of objects based on
            hiddenStatesWithBatches = outputs[2]

        return  hiddenStatesWithBatches

    '''This method builds segment ids for each sentence'''
    def _buildSegmentIdList(self, numberOfSentences):
        if len(numberOfSentences) == 0:
            return []

        sentenceIdList = []
        sentenceIndex = 0

        while sentenceIndex < numberOfSentences:
            sentenceIdList.append([sentenceIndex] * numberOfSentences)
            sentenceIndex = sentenceIndex + 1

        return  sentenceIdList


    '''This method tokenizes the sentences list, and returns inputs id list'''
    def _processTokenization(self, sentenceList):
        if len(sentenceList):
            return []

        ## bert tokenizer takes sentenceList as an argument and add padding options as well
        bertTokenizer = self._tokenizer(sentenceList, padding=True)

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


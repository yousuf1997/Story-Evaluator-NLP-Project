
'''
    This class will process the evaluation of the story based on the method
    proposed in the paper. Here where we will utilize all neccessary tools such
    as BertProcessor and other utills
'''
from bert.BertProcessor import BertProcessor
from utills.SentenceUtill import SentenceUtill
from utills.StopWordUtill import StopWordsUtill
from utills.VectorUtill import VectorUtill


class StoryQualityEvaluator:

    def __init__(self):
        # bert processor
        self.bert = BertProcessor()
        # stopwords utils to remove stop words on each sentence
        # will do the sentence processing prior to utilizing this util
        self._STOP_WORD_UTILL = StopWordsUtill()
        # sentence utils for extracting the sentences from the paragraph
        self._SENTENCE_UTIL = SentenceUtill()
        # vector utils
        self._VECTOR_UTILL = VectorUtill();
        # batch
        self._bertComputedSentences = []

    def initiateBertProcess(self, story):

        if len(story) == 0:
            return

        ## perform sentence breaking
        sentenceList = self._SENTENCE_UTIL.extractSentencesFromParagraph(story)
        ## clear the bertComputedSentences
        self._bertComputedSentences = []

        ## we need to process three sentences at a time
        index = 0
        sentenceIndex = 0

        while index < len(sentenceList):
            rawBatchList = sentenceList[index:index+3]
            nonStopWordBatchList = self._removeStopWordsForBatch(rawBatchList)
            self.bert.process(nonStopWordBatchList)
            wordVectorList = self.bert.getWordVectorListByBatch()
            self._appendComputedBatches(rawBatchList, nonStopWordBatchList, wordVectorList)
            index = index + 3

    '''WIP : this has some issue! need to check the vector addition!'''
    def computeMovingCosineSimilarity(self):

        ## start from second sentence
        sentenceIndex = 1

        ## add all vectors in the first sentence
        sumVector = []
        wordVectorList = self._bertComputedSentences[0]["vector_values"]
        for wordVector in wordVectorList:
            ## get the vector
            keys = wordVector.keys()
            for key in keys:
                sumVector = self._VECTOR_UTILL.performVectorArthimetic(sumVector, wordVector[key], "ADD")

        while sentenceIndex < len(self._bertComputedSentences):
            ## in the current sentence traverse the vector
            wordVectorList = self._bertComputedSentences[sentenceIndex]["vector_values"]
            cosineSimilarityList = []
            for wordVector in wordVectorList:
                ## get the vector
                keys = wordVector.keys()
                for key in keys:
                    ## compute moving cosine
                    cosineSimilarity = self._VECTOR_UTILL.computeCosineSimilarity(sumVector, wordVector[key])
                    ## add the current vector into the word vector for next computation
                    sumVector = self._VECTOR_UTILL.performVectorArthimetic(sumVector, wordVector[key], "ADD")
                    ## add the similarity to the list
                    cosineSimilarityList.append(cosineSimilarity)
            ## add the cosine list to the bert sentence list
            self._bertComputedSentences[sentenceIndex]["moving_cosine_similarity"].append(cosineSimilarityList)
            ## append next index
            sentenceIndex = sentenceIndex + 1
        print(self._bertComputedSentences)

    def _removeStopWordsForBatch(self, rawBatchList):
        nonStopWordBatchList = []
        for batch in rawBatchList:
            nonStopWordBatchList.append(self._STOP_WORD_UTILL.removeStopWords(batch))
        return nonStopWordBatchList

    def _appendComputedBatches(self, rawBatchList, nonStopWordBatchList, wordVectorList):
        index = 0
        while index < len(rawBatchList):
            computedSentences = {}
            computedSentences["raw_batch"] = rawBatchList[index]
            computedSentences["non_stop_word_batch"] = nonStopWordBatchList[index]
            computedSentences["vector_values"] = wordVectorList[index]
            computedSentences["moving_cosine_similarity"] = []
            self._bertComputedSentences.append(computedSentences)
            index = index + 1


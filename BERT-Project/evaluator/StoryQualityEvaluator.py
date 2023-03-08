
'''
    This class will process the evaluation of the story based on the method
    proposed in the paper. Here where we will utilize all neccessary tools such
    as BertProcessor and other utills
'''
from bert.BertProcessor import BertProcessor
from utills.SentenceUtill import SentenceUtill
from utills.StopWordUtill import StopWordsUtill


class StoryQualityEvaluator:

    def __init__(self):
        # bert processor
        self.bert = BertProcessor()
        # stopwords utils to remove stop words on each sentence
        # will do the sentence processing prior to utilizing this util
        self._STOP_WORD_UTILL = StopWordsUtill()
        # sentence utils for extracting the sentences from the paragraph
        self._SENTENCE_UTIL = SentenceUtill()
        # batchH
        self._bertComputedSentences = []

    def initiateBertProcess(self, story):

        if len(story) == 0:
            return

        ## perform sentence breaking
        sentenceList = self._SENTENCE_UTIL.extractSentencesFromParagraph(story)

        ## we need to process three sentences at a time
        index = 0
        sentenceIndex = 0

        while index < len(sentenceList):
            rawBatchList = sentenceList[index:index+3]
            nonStopWordBatchList = self._removeStopWordsForBatch(rawBatchList)
            self.bert.process(nonStopWordBatchList)
            wordVectorList = self.bert.getWordVectorListByBatch()
            print("Raw ", rawBatchList)
            print("Non Stop", nonStopWordBatchList)
            print("Word Vectors ", wordVectorList)
            self._appendComputedBatches(rawBatchList, nonStopWordBatchList, wordVectorList)
            index = index + 3
        print(self._bertComputedSentences)

    def _removeStopWordsForBatch(self, rawBatchList):
        nonStopWordBatchList = []
        for batch in rawBatchList:
            nonStopWordBatchList.append(self._STOP_WORD_UTILL.removeStopWords(batch))
        return nonStopWordBatchList

    def _appendComputedBatches(self, rawBatchList, nonStopWordBatchList, wordVectorList):
        computedSentences = {}
        computedSentences["raw_batch"] = rawBatchList
        computedSentences["non_stop_word_batch"] = nonStopWordBatchList
        computedSentences["vector_values"] = wordVectorList
        self._bertComputedSentences.append(computedSentences)



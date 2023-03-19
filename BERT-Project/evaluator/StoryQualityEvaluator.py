
'''
    This class will process the evaluation of the story based on the method
    proposed in the paper. Here where we will utilize all neccessary tools such
    as BertProcessor and other utills
'''
import math

from bert.BertProcessor import BertProcessor
from utills.EntityRemoverUtill import EntityRemoverUtill
from utills.OutlierUtill import OutlierUtill
from utills.SentenceUtill import SentenceUtill
from utills.StopWordUtill import StopWordsUtill
from utills.VectorUtill import VectorUtill
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.spatial import distance
from sklearn.metrics.pairwise import cosine_similarity

class StoryQualityEvaluator:

    def __init__(self):
        # bert processor
        self.bert = BertProcessor()
        # stopwords utils to remove stop words on each sentence
        # will do the sentence processing prior to utilizing this util
        self._STOP_WORD_UTILL = StopWordsUtill()
        # sentence utils for extracting the sentences from the paragraph
        self._SENTENCE_UTIL = SentenceUtill()
        # entity remover utill
        self._ENTITY_REMOVER_UTILL = EntityRemoverUtill()
        # vector utils
        self._VECTOR_UTILL = VectorUtill();
        ## outlier util
        self._OUTLIER_UTILL =  OutlierUtill()
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
            nonEntityBatchList = self._ENTITY_REMOVER_UTILL.removeEntities(rawBatchList)
            nonStopWordBatchList = self._removeStopWordsForBatch(nonEntityBatchList)
            self.bert.process(nonStopWordBatchList)
            wordVectorList = self.bert.getWordVectorListByBatch()
            self._appendComputedBatches(rawBatchList, nonStopWordBatchList, nonEntityBatchList, wordVectorList)
            index = index + 3

    def computeMovingCosineSimilarity(self):

        ## start from second sentence
        sentenceIndex = 1
        meanVector = []
        startingWordBFromSentenceTwo = ''

        while sentenceIndex < len(self._bertComputedSentences):
            ## in the current sentence traverse the vector
            wordVectorList = self._bertComputedSentences[sentenceIndex]["vector_values"]
            cosineSimilarityList = []
            for wordVector in wordVectorList:
                ## get the vector
                keys = wordVector.keys()
                for key in keys:
                    ##testing code
                    if len(meanVector) == 0:
                        ## push the current vector into the meanvector
                        meanVector.append(wordVector[key])
                        startingWordBFromSentenceTwo = key
                    meanVectorValue = np.mean(meanVector ,axis=0,dtype=np.float64).tolist()
                    ## compute moving cosine similarity
                    cosineSimilarityTest = 1 - distance.cosine(meanVectorValue, wordVector[key])
                    ## append the current key for next processing
                    meanVector.append(wordVector[key])
                    ## add the similarity to the list
                    ##cosineSimilarityList.append(key+"_"+str(cosineSimilarity))
                    cosineSimilarityList.append(float(cosineSimilarityTest))

            ## add the cosine list to the bert sentence list
            self._bertComputedSentences[sentenceIndex]["moving_cosine_similarity"] = cosineSimilarityList
            ## append next index
            sentenceIndex = sentenceIndex + 1

            ## calculate the cosine for the first b
            meanVector.pop(0)
            ## get the vector
            bVector = self._bertComputedSentences[1]['vector_values'][0][startingWordBFromSentenceTwo]
            meanVectorValue = np.mean(meanVector ,axis=0,dtype=np.float64).tolist()
            cSim = 1 - distance.cosine(meanVectorValue, bVector)
            self._bertComputedSentences[1]['moving_cosine_similarity'][0]=cSim


    def plotCosineSimilaritiesBySentenceWord(self):
        x_axis = []
        y_axis = []
        self._flattenMapOfWordAndConsineSimlarities = []
        for index, sentenceData in enumerate(self._bertComputedSentences):
            cosineSimList = sentenceData['moving_cosine_similarity']
            wordList = sentenceData["vector_values"]

            for wordIndex,cosineData in enumerate(cosineSimList):
                x_axis.append(str(index + 1) + "_" + list(wordList[wordIndex].keys())[0])
                y_axis.append(float(cosineData))
                flattenData = {}
                flattenData['sentenceIndex'] = str(index)
                flattenData['word'] = str(list(wordList[wordIndex].keys())[0])
                flattenData['similarityScore'] = float(cosineData)
                flattenData['wordIndex'] = wordIndex
                self._flattenMapOfWordAndConsineSimlarities.append(flattenData)

        outlierMap = self._OUTLIER_UTILL.calculateOutlier(y_axis.copy())
        ## store that in outlier map
        self._outlierMap = outlierMap
        ## plot the graph
        copyList = y_axis.copy()
        copyList.sort()
        fig = plt.figure()
        fig.subplots_adjust(top=0.85)
        # Set titles for the figure and the subplot respectively
        plt.plot(range(len(x_axis)), y_axis, color='green')
        plt.axhline(y = outlierMap["lowerBound"], color = 'r', linestyle = 'dashed')
        plt.axhline(y = outlierMap["upperBound"] if outlierMap["upperBound"] <= 1 else 1, color = 'b', linestyle = 'dashed')
        plt.title("Moving cosine similarity")
        plt.ylabel("Cosine Similarity")
        plt.xlabel("Words by sentence")
        plt.xticks(ticks=range(len(x_axis)), labels=x_axis, rotation = 90)
        M_SCORE = self._searchForOutlierAndComputerQuantitativeMeasure()
        fig.suptitle('Outlier Bounds [Lower Bound : ' + str(outlierMap["lowerBound"]) + " , Upper Bound : " + str(outlierMap["upperBound"]) + " ], M = " + str(M_SCORE), fontsize=12, fontweight='bold')
        plt.show()


    def _searchForOutlierAndComputerQuantitativeMeasure(self):
        ## need to find outliers from exactly two sentences
        index = 0
        outlierMap = []
        ## check if the are same two different sentence
        sentenceCount = 0
        previousSentenceIndex = ''
        index = 0

        while index < len(self._flattenMapOfWordAndConsineSimlarities):
            currentData = self._flattenMapOfWordAndConsineSimlarities[index]
            currentScore = currentData['similarityScore']
            if currentScore < self._outlierMap['lowerBound'] or currentScore > self._outlierMap['upperBound']:
                outlierMap.append(currentData)
            index = index + 1

        print('Outlier : ', outlierMap)

        while index < len(outlierMap):
            currentSentenceIndex = int(outlierMap[index]['sentenceIndex'])
            if index == 0:
                previousSentenceIndex = currentSentenceIndex
                sentenceCount = sentenceCount + 1
            if previousSentenceIndex != currentSentenceIndex:
                sentenceCount = sentenceCount + 1
                previousSentenceIndex = currentSentenceIndex
            index = index + 1

        if sentenceCount == 2:
            print("We have outliers are from exactly two sentence.")
        elif sentenceCount > 2 or sentenceCount < 2:
            print("We have outliers are from more than two sentence or less than two sentence or no outlier")
        return 0.0


    def _removeStopWordsForBatch(self, rawBatchList):
        nonStopWordBatchList = []
        for batch in rawBatchList:
            nonStopWordBatchList.append(self._STOP_WORD_UTILL.removeStopWords(batch))
        return nonStopWordBatchList

    def _appendComputedBatches(self, rawBatchList, nonStopWordBatchList, nonEntityBatchList, wordVectorList):
        index = 0
        while index < len(rawBatchList):
            computedSentences = {}
            computedSentences["raw_batch"] = rawBatchList[index]
            computedSentences["non_entity_batch"] = nonEntityBatchList[index]
            computedSentences["non_stop_word_batch"] = nonStopWordBatchList[index]
            computedSentences["vector_values"] = wordVectorList[index]
            computedSentences["moving_cosine_similarity"] = []
            self._bertComputedSentences.append(computedSentences)
            index = index + 1


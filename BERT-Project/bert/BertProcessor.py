import torch
from transformers import BertTokenizer, BertModel

from utills.SentenceUtill import SentenceUtill
from utills.StopWordUtill import StopWordsUtill

'''
    This class represent the bert model for the word embedding, and all the transformation stuff happens here
    Make sure the transform is installed
'''
class BertProcessor:

    def __init__(self):
        # Load pre-trained model tokenizer (vocabulary)
        self._tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
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

        ## tokens
        tokens = self._removeStopWordsAndTokenizeSentences(sentenceList)


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
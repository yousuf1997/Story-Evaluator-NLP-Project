import spacy

'''
    This class removes named entity using spacy API
    Installation of the spacy is required:
    -  pip3 install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz
    -  python -m spacy download en_core_web_sm
'''


class EntityRemoverUtill:

    def __init__(self):
        self._ENTITY_ANALYZER = spacy.load('en_core_web_sm')

    def removeEntities(self, sentenceList):
        if len(sentenceList) == 0:
            return []
        nonEntitySentences = []
        for sentence in sentenceList:
            document = self._ENTITY_ANALYZER(sentence)
            nonEntitySentences.append(self._removeEntities(sentence, document))
        return nonEntitySentences
    def _removeEntities(self, sentence : str, document):
        if len(sentence) == 0:
            return ""
        for ent in document.ents:
            sentence = sentence.replace(str(ent.text), '')
        return sentence.replace('  ', ' ')

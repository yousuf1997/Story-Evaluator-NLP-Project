
'''This class will parse paragraph into sentences'''
class SentenceUtil:

    def __int__(self):
        pass

    @staticmethod
    def extractSentencesFromParagraph(self, paragraph: str) -> list:
        sentenceList = []
        charIndex = 0
        currentSentence = ""

        while charIndex < len(paragraph):
            currentChar = paragraph[charIndex]
            ### append the charc
            currentSentence = currentSentence + currentChar
            if self._isSentenceEnding(currentChar):
                ## push the sentence to the list
                sentenceList.append(currentSentence)
                ## reset for new sentence to the
                currentSentence = ""
        ## append the last sentence
        if len(currentSentence) > 0:
            sentenceList.append(currentSentence)
        return sentenceList

    @staticmethod
    def _isSentenceEnding(self, char:str):
        endingPunctuations = [".", ",", "!"]
        if char in endingPunctuations:
            return True
        return False

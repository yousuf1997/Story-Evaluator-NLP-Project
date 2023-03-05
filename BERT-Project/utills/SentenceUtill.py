
'''This class will parse paragraph into sentences'''
class SentenceUtill:

    def __int__(self):
        pass


    def extractSentencesFromParagraph(self, paragraph: str) -> list:
        sentenceList = []
        charIndex = 0
        currentSentence = ""
        print("SentenceUtill.extractSentencesFromParagraph >> Sentence processing begins.")
        while charIndex < len(paragraph):
            currentChar = paragraph[charIndex]
            ### append the charc
            currentSentence = currentSentence + currentChar
            if self._isSentenceEnding(currentChar):
                ## push the sentence to the list
                sentenceList.append(currentSentence)
                ## reset for new sentence to the
                currentSentence = ""
            ## append the index
            charIndex = charIndex + 1
        ## append the last sentence
        if len(currentSentence) > 0:
            sentenceList.append(currentSentence)
        print("SentenceUtill.extractSentencesFromParagraph >> Sentence processed, and total of", len(sentenceList) , "sentences found")
        return sentenceList

    def _isSentenceEnding(self, char:str):
        endingPunctuations = [".", "?", "!"]
        if char in endingPunctuations:
            return True
        return False

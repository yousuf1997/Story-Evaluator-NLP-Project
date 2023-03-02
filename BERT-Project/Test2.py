from utills.SentenceUtill import SentenceUtill
from utills.StopWordUtill import StopWordsUtill

paragraph = "I went to college on monday. I took korahs class, he was a monster." \
          "Today is it tuesday? Oh! my bad today is not tuesday. I was in college. Welcome to party"

sentenceUtill = SentenceUtill()
stopWordUtill = StopWordsUtill()


sentenceList = sentenceUtill.extractSentencesFromParagraph(paragraph)

index = 0

while index < len(sentenceList):
    currentSentence = sentenceList[index]
    print("Before : ", currentSentence)
    print("After : ", str(stopWordUtill.removeStopWords(currentSentence)))
    index = index + 1




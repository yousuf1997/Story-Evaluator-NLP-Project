import dataclasses

'''
    This class represents word, position number, and sentence number
'''

@dataclasses
class Word:
    wordText: str
    sentenceId: int
    wordPositionInSentence: int
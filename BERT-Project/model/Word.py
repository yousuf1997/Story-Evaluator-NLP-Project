import dataclasses

'''
    This class represents word, position number, and sentence number
'''

@dataclasses
class Word:
    wordText: str
    token: int
    sentenceId: int
    positionInSentence: int
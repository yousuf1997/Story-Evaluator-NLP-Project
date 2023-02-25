import dataclasses

'''
    This class represents word, position number, and sentence number
'''

@dataclasses
class Word:
    wordText: str
    token: str ### this token is created after feeding the sentence to the tokenizer!
    tokenId:int
    segmentId: int
    positionInSentence: int
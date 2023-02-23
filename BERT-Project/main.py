from utills.SentenceUtill import SentenceUtill
from utills.VectorUtill import VectorUtill

sentenceUtill = SentenceUtill()
vectorUtill = VectorUtill()

## test sentence breaker
text = 'So yesterday I was there. But i do no know what happend, so i left. on Monday I was like What! Do you know what? so tuesday I was like whatever.'
expectedList = ['So yesterday I was there.', ' But i do no know what happend, so i left.', ' on Monday I was like What!', ' Do you know what?', ' so tuesday I was like whatever.']

assert expectedList == sentenceUtill.extractSentencesFromParagraph(text)


## test cosine similarity method
docVectorOne = [1,1,1,1,1,0,0]
docVectorTwo = [0,0,1,1,0,1,1]


assert 0.44721 == round(vectorUtill.computeCosineSimilarity(docVectorOne,docVectorTwo), 5)

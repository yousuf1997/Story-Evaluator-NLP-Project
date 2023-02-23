from utills.SentenceUtill import SentenceUtill

sentenceUtill = SentenceUtill()

text = 'So yesterday I was there. But i do no know what happend, so i left. on Monday I was like What! Do you know what? so tuesday I was like whatever.'

'''
  Expected 
  ['So yesterday I was there.', ' But i do no know what happend, so i left.', ' on Monday I was like What!', ' Do you know what?', ' so tuesday I was like whatever.']
'''
print(sentenceUtill.extractSentencesFromParagraph(text))

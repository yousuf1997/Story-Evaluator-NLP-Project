# CS-5990-Term-Project
This repo contains code which implements the method discussed in the following paper : https://ojs.aaai.org/index.php/AIIDE/article/view/5217 as a part of CS-5990 course's term project from my graduate school (CSU Pomona)

### Dependency Libraries 
```
pip install torch 
pip install matplotlib
pip install transformers
pip install scipy
pip install https://github.com/explosion/spacymodels/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz
python -m spacy download en_core_web_sm
```
### Driver File
BertTest.py is the driver file to execute the program. Sample call to run the program
```
from evaluator.StoryQualityEvaluator import StoryQualityEvaluator

## bertProcessor = BertProcessor()
storyQualityEvaluator = StoryQualityEvaluator()

storyQualityEvaluator.initiateBertProcess(STORY_TEXT)
storyQualityEvaluator.computeMovingCosineSimilarity()
storyQualityEvaluator.plotCosineSimilaritiesBySentenceWord()
```


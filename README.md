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

storyQualityEvaluator = StoryQualityEvaluator()

storyQualityEvaluator.initiateBertProcess(STORY_TEXT)
storyQualityEvaluator.computeMovingCosineSimilarity()
storyQualityEvaluator.plotCosineSimilaritiesBySentenceWord()
```
The above command will produce a graph with plotting the running cosine similarity. 

### Sample Story and Results 
#### Story
```
Shahjahan, the Mughal emperor, sat on his throne, lost in thought. His mind was consumed with grief and longing for his beloved wife, Mumtaz Mahal, who had passed away years ago. He yearned for a way to immortalize her memory, to create a monument that would stand the test of time and serve as a testament to their love. And so, he decided to build a grand mausoleum in her honor, unlike anything the world had ever seen. He commissioned the finest architects, craftsmen, and artisans to construct what would become known as the Taj Mahal. Years went by as the magnificent structure slowly took shape, rising from the ground like a shimmering ivory dream. Shahjahan poured all his love and passion into the project, often visiting the site to oversee the construction himself. Finally, the day arrived when the Taj Mahal was completed. Shahjahan stood before it, tears streaming down his face, as he gazed upon the breathtaking sight. As he turned to leave, he realized that his own legacy was now forever linked to the monument. And so, he whispered to himself, Let this monument be not just a tribute to my wife, but also a symbol of the grandeur of the Mughal Empire. And with that, Shahjahan walked away, leaving behind a legacy that would inspire generations to come.
```
#### Results
![Results of running the above story.](https://github.com/yousuf1997/CS-5990-Term-Project/blob/main/StoryQualityEvaluator/experiment-results/Result_1.png)

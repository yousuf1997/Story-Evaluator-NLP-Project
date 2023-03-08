from bert.BertProcessor import BertProcessor
from evaluator.StoryQualityEvaluator import StoryQualityEvaluator
from utills.VectorUtill import VectorUtill
from scipy.spatial.distance import cosine

## bertProcessor = BertProcessor()
storyQualityEvaluator = StoryQualityEvaluator()

vector = VectorUtill()

paragraph = "welcome to the bank vault." \
            "The bank robber was seen fishing on the Mississippi river bank." \
            "I just have credit card of bank of america." \
            "I just have credit card of bank of america." \
             "Yesterday was i went to rob the bank." \
            "Yesterday was i went to rob the bank."
storyQualityEvaluator.initiateBertProcess(paragraph)
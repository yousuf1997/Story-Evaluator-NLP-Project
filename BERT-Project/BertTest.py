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

paragraph1 ="Sam and Judy went out for dinner at their favorite restaurant. While driving to the restaurant, Judy’s favorite song played on the radio. Sam found a parking space at the very front of the restaurant. Sam and Judy were seated immediately and ordered their favorite food to the waiter. He looked distracted and tired but was polite while taking their order. Sam’s favorite song played on the radio while they waited for their food. When the waiter returned with their food it was all wrong! The waiter apologized and returned a few minutes later with the correct order. Sam and Judy enjoyed their meal. They paid their tab, left a tip for the waiter, and drove back home."

storyQualityEvaluator.initiateBertProcess(paragraph1)

storyQualityEvaluator.computeMovingCosineSimilarity()
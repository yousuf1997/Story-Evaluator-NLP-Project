from bert.BertProcessor import BertProcessor
from evaluator.StoryQualityEvaluator import StoryQualityEvaluator
from utills.VectorUtill import VectorUtill
from scipy.spatial.distance import cosine

## bertProcessor = BertProcessor()
storyQualityEvaluator = StoryQualityEvaluator()

vector = VectorUtill()

p = "Sam and Judy went out for dinner at their favorite restaurant. While driving to the restaurant, Judy’s favorite song played on the radio. Sam found a parking space at the very front of the restaurant. Sam and Judy were seated immediately and ordered their favorite food to the waiter. He looked distracted and tired but was polite while taking their order. Sam’s favorite song played on the radio while they waited for their food. When the waiter returned with their food it was all wrong! The waiter apologized and returned a few minutes later with the correct order. Sam and Judy enjoyed their meal. They paid their tab, left a tip for the waiter, and drove back home."
p2 = "Twenty-two, I was with my first lover, not college-girl exploring but the real deal. She was 28 and had an even older long-distance partner who was visiting, so we went out for coffee drinks. Playing just friends. I’d never had one before; it was divine, sweet Bailey’s flame searing night mocha, whipped cream-topped glass mug, shaved chocolate. Her partner paid, magnanimous, husky and tanned, clueless or so it seemed. I was smug, silky, sitting back watching my lover managing. Later, when she cheated on me too, I called her partner, trying to commiserate. And that was some hot wet salt."
p3 = "Curiosity and intrigue lifelong companions. Shell question everything, even the origin of trees. She fears them at night when the wind races through like a freight train mimicking the clamoring and wailing of voices."
p4 = "She arrived with clenched fists, wide eyes, and strong lungs. During the cleaning, the elders caught her stretching her neck, peering into the darkness of a near past. This would be her lot in life: a bellowing voice, roaming eyes, and a sankofa spirit. Curiosity and intrigue lifelong companions. She’ll question everything, even the origin of trees. She fears them at night when the wind races through like a freight train mimicking the clamoring and wailing of voices. She’ll demand to know who’s there and consider each tap, scratch, and drag a clue, a direct path to the other side."
text = "After stealing money from the bank vault, the bank robber was seen " \
       "fishing on the Mississippi river bank."
storyQualityEvaluator.initiateBertProcess(p)
storyQualityEvaluator.computeMovingCosineSimilarity()
storyQualityEvaluator.plotCosineSimilaritiesBySentenceWord()
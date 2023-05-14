from evaluator.StoryQualityEvaluator import StoryQualityEvaluator

storyQualityEvaluator = StoryQualityEvaluator()

story = "Amelia explored an abandoned mansion, discovering a warning in an old book about a treacherous mirror. Ignoring it, she gazed into the mirror, unknowingly releasing a malevolent entity. Her reflection grew wicked, pushing her toward darkness. Now, she fights to reclaim her true self and overcome the unleashed evil."

storyQualityEvaluator.initiateBertProcess(story)
storyQualityEvaluator.computeMovingCosineSimilarity()
storyQualityEvaluator.plotCosineSimilaritiesBySentenceWord()
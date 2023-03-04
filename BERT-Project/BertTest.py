from bert.BertProcessor import BertProcessor

bertProcessor = BertProcessor()

paragraph = "After stealing money from the bank vault, the bank robber was seen " \
       "fishing on the Mississippi river bank. Yesterday was i went to rob the bank." \
       "John got good career, and making bank."

bertProcessor.process(paragraph)

print(bertProcessor.getWordVectorListByBatch())
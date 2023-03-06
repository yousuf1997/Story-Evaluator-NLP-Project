from bert.BertProcessor import BertProcessor

bertProcessor = BertProcessor()

paragraph = "After stealing money from the bank vault, the bank robber was seen " \
       "fishing on the Mississippi river bank. Yesterday was i went to rob the bank." \
       "John got good career, ankdhd making bank kutikas."

bertProcessor.process(paragraph)

print(bertProcessor.getWordVectorListByBatch())

### vector values are same for all the words, Need to check the bug!
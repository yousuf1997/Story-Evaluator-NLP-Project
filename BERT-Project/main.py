import torch
from transformers import BertTokenizer, BertModel

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Define a new example sentence with multiple meanings of the word "bank"
text = "After stealing money from the bank vault, the bank robber was seen " \
       "fishing on the Mississippi river bank."

text2 = "Yesterday was i went to bank to get money, later i went to river bank"

# Add the special tokens.
marked_text1 = "[CLS] " + text + " [SEP]"
marked_text2 = " " + text2

# Split the sentence into tokens.
tokenized_text1 = tokenizer.tokenize(marked_text1)
tokenized_text2 = tokenizer.tokenize(marked_text2)

## seg ments

# Map the token strings to their vocabulary indeces.
indexed_tokens1 = tokenizer.convert_tokens_to_ids(tokenized_text1)
indexed_tokens2 = tokenizer.convert_tokens_to_ids(tokenized_text2)

segment1 = [0] * len(indexed_tokens1)
segment2 = [1] * len(indexed_tokens2)


# for tup in zip(tokenized_text1, indexed_tokens1):
#     print('{:<12} {:>6,}'.format(tup[0], tup[1]))
#
# print("breaking!")
#
# for tup in zip(tokenized_text2, indexed_tokens2):
#     print('{:<12} {:>6,}'.format(tup[0], tup[1]))


tokens_tensor = torch.tensor([indexed_tokens1])
segments_tensors = torch.tensor([segment1])

# Load pre-trained model (weights)
model = BertModel.from_pretrained('bert-base-uncased', output_hidden_states = True)

# Put the model in "evaluation" mode, meaning feed-forward operation.
model.eval()


# Run the text through BERT, and collect all of the hidden states produced
# from all 12 layers.
with torch.no_grad():

       outputs = model(tokens_tensor, segments_tensors)

       # Evaluating the model will return a different number of objects based on
       # how it's  configured in the `from_pretrained` call earlier. In this case,
       # becase we set `output_hidden_states = True`, the third item will be the
       # hidden states from all layers. See the documentation for more details:
       # https://huggingface.co/transformers/model_doc/bert.html#bertmodel
       hidden_states = outputs[2]

print(hidden_states)
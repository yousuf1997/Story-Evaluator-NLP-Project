import torch
from transformers import BertTokenizer, BertModel

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Define a new example sentence with multiple meanings of the word "bank"
text = "After stealing money from the bank vault, the bank robber was seen " \
       "fishing on the Mississippi river bank."

text2 = "Yesterday was i went to rob the bank."

text3 = "John got good career, and making bank"

sentences = [text, text2, text3]

tokenized = tokenizer(sentences, padding=True)

input_ids = tokenized["input_ids"]

lengthOfArray = len(input_ids[0])

segment_ids = [[0] * lengthOfArray, [1] * lengthOfArray, [2] * lengthOfArray]

# Convert inputs to PyTorch tensors
tokens_tensor = torch.tensor(input_ids)
segments_tensors = torch.tensor(segment_ids)

# Load pre-trained model (weights)
model = BertModel.from_pretrained('bert-base-uncased',output_hidden_states = True)

# Put the model in "evaluation" mode, meaning feed-forward operation.
model.eval()

# Run the text through BERT, and collect all of the hidden states produced
# from all 12 layers.
with torch.no_grad():

       outputs = model(tokens_tensor, segments_tensors)

       # Evaluating the model will return a different number of objects based on
       hidden_states = outputs[2]



print ("Number of layers:", len(hidden_states), "  (initial embeddings + 12 BERT layers)")
layer_i = 0

print ("Number of batches:", len(hidden_states[layer_i]))
batch_i = 0

print ("Number of tokens:", len(hidden_states[layer_i][batch_i]))
token_i = 0

print ("Number of hidden units:", len(hidden_states[layer_i][batch_i][token_i]))

# Concatenate the tensors for all layers. We use `stack` here to
# create a new dimension in the tensor.
token_embeddings = torch.stack(hidden_states, dim=0)
# Remove dimension 1, the "batches".
# token_embeddings = token_embeddings.permute(2,0,2)

# Stores the token vectors, with shape [22 x 768]
token_vecs_sum = []

# `token_embeddings` is a [22 x 12 x 768] tensor.

# For each token in the sentence...
for token in token_embeddings:

       # `token` is a [12 x 768] tensor
       # Sum the vectors from the last four layers.
       sum_vec = torch.sum(token[-4:], dim=0)

       # Use `sum_vec` to represent `token`.
       token_vecs_sum.append(sum_vec)

# Stores the token vectors, with shape [22 x 768]
token_vecs_sum = []

# `token_embeddings` is a [22 x 12 x 768] tensor.

# For each token in the sentence...
for token in token_embeddings:

       # `token` is a [12 x 768] tensor
       # Sum the vectors from the last four layers.
       sum_vec = torch.sum(token[-4:], dim=0)

       # Use `sum_vec` to represent `token`.
       token_vecs_sum.append(sum_vec)

print ('Shape is: %d x %d' % (len(token_vecs_sum), len(token_vecs_sum[0])))
print('First 5 vector values for each instance of "bank".')
print('')
print("bank vault   ", str(token_vecs_sum[0][6][:5]))

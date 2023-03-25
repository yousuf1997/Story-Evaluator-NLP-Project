import torch
from transformers import BertTokenizer, BertModel

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokenizer2 = BertTokenizer.from_pretrained('bert-base-uncased')

# Define a new example sentence with multiple meanings of the word "bank"
text = "After stealing money from the bank vault, the bank robber was seen " \
       "fishing on the Mississippi river bank."

text2 = "Yesterday was i went to rob the bank."

text3 = "John got good career, and making bank."

text4 = "There was couple of banks."

text5 = "There was couple of banks."

sentences = [text, text2, text3, text4, text5]

tokenized = tokenizer(sentences, padding=True)

input_ids = tokenized["input_ids"]

print("Input ids ", input_ids)

lengthOfArray = len(input_ids[0])

## for each sentences
segment_ids = [[0] * lengthOfArray, [1] * lengthOfArray, [2] * lengthOfArray, [3] * lengthOfArray, [4] * lengthOfArray]

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


# print ("Number of layers:", len(hidden_states), "  (initial embeddings + 12 BERT layers)")
# layer_i = 0
#
# print ("Number of batches:", len(hidden_states[layer_i]))
# batch_i = 0
#
# print ("Number of tokens:", len(hidden_states[layer_i][0]))
# print ("Number of tokens:", len(hidden_states[layer_i][1]))
# print ("Number of tokens:", len(hidden_states[layer_i][2]))
# print ("Number of tokens:", len(hidden_states[layer_i][3]))
# print("Sentece three tokens ", tokenizer2.convert_ids_to_tokens(input_ids[3]))
#
# token_i = 0
#
# print ("Number of hidden units:", len(hidden_states[layer_i][batch_i][token_i]))
# ## get the layers of the first batch only -- do for each batch
# first_batch_hidden_states = []
# print("Hidden states", len(hidden_states))
# for states in hidden_states:
#        print("Process ", len(states))
#        print("process s", len(states[0]))
#        first_batch_hidden_states.append(states[0])

# Concatenate the tensors for all layers. We use `stack` here to
# create a new dimension in the tensor.
print("Welcome ", len(hidden_states))

## merge the hidden states for the first batch only
first_batch_hidden_states = []

for states in hidden_states:
       first_batch_hidden_states.append(states[0])

token_embeddings = torch.stack(first_batch_hidden_states, dim=0)
token_embeddings = torch.squeeze(token_embeddings, dim=1)
print("TEST2", len(token_embeddings))

token_embeddings = token_embeddings.permute(1,0,2)
# Remove dimension 1, the "batches".
# token_embeddings = token_embeddings.permute(2,0,2)
# print("Welcome ", len(hidden_states[0]))
#
# ## merge the hidden states for the first batch only
# first_batch_hidden_states = []
#
# for states in hidden_states:
#        first_batch_hidden_states.append(states[0])
print("permuted size ", token_embeddings.size())
## merged_first_sentence_states = torch.stack(first_batch_hidden_states)
# Swap dimensions 0 and 1.
## torch.Size([13, 4, 22, 768])

# Stores the token vectors, with shape [22 x 768]
token_vecs_sum = []
# `token_embeddings` is a [22 x 12 x 768] tensor.

print("token embedding" , len(token_embeddings))


# For each token in the sentence...
for token in token_embeddings:

       # `token` is a [12 x 768] tensor
       # Sum the vectors from the last four layers.
       print("Length is ", len(token))
       sum_vec = torch.sum(token[-4:], dim=0)
       # Use `sum_vec` to represent `token`.
       token_vecs_sum.append(sum_vec)



print("TET ", len(token_vecs_sum))
print('First 5 vector values for each instance of "bank".')
print('')
print("bank vault   ", str(token_vecs_sum[6][:5]))
print("bank robber  ", str(token_vecs_sum[10][:5]))
print("river bank   ", str(token_vecs_sum[19][:5]))


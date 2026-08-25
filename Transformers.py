#Transformers 
#A Transformer is a deep learning architecture that processes sequential data using a mechanism called Self-Attention. 
# It was introduced in the paper "Attention Is All You Need" (2017) and is widely used in 
# Natural Language Processing (NLP), computer vision, and generative AI models such as GPT, BERT, and T5.

#Unlike RNNs and LSTMs, Transformers process all input elements in parallel,
#making training faster and more efficient.
#------------------------------------------------------------------------------------------------------------------------
import numpy as np

# Give Input sequence
sentence = input("Enter numbers separated by space: ")
X = np.array([list(map(float, sentence.split()))])

# Transpose for matrix operations
X = X.T

# Giving Dimension
d_model = X.shape[0]

# Random weights
Wq = np.random.rand(d_model, d_model)
Wk = np.random.rand(d_model, d_model)
Wv = np.random.rand(d_model, d_model)

# Query, Key, Value
Q = np.dot(Wq, X)
K = np.dot(Wk, X)
V = np.dot(Wv, X)

# Making Attention Scores
scores = np.dot(Q.T, K)

# On Scaling
scores = scores / np.sqrt(d_model)

# Softmax Calculate
scores = scores - np.max(scores, axis=1, keepdims=True)
exp_scores = np.exp(scores)
attention_weights = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

# Use Attention Output
output = np.dot(attention_weights, V.T)

print("\nAttention Weights:")
print(attention_weights)

print("\nTransformer Output:")
print(output)
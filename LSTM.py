#Long-Short Term Memory
#LSTM (Long Short-Term Memory) is a special type of Recurrent Neural Network (RNN) 
#designed to learn and remember information over long sequences of data.
#It solves the vanishing gradient problem of traditional
#RNNs by using a memory cell and gating mechanisms.

#LSTMs are widely used for:

#Time series forecasting
#Stock price prediction
#Speech recognition
#Machine translation
#Sentiment analysis
#Text generation
#Components of an LSTM Cell

#An LSTM cell contains:

#Cell State (Cₜ): Long-term memory.
#Hidden State (Hₜ): Short-term memory/output.
#Forget Gate (Fₜ): Decides what information to discard.
#Input Gate (Iₜ): Decides what new information to store.
#Candidate Memory (Ĉₜ): New candidate values for memory.
#Output Gate (Oₜ): Decides what information to output.
#--------------------------------------------------------
import numpy as np

# Using Activation Functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

class LSTM:
    def __init__(self, input_size, hidden_size):
        self.hidden_size = hidden_size

        self.Wf = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wi = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wc = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wo = np.random.randn(hidden_size, hidden_size + input_size)

        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bc = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))

    def forward(self, inputs):
        h = np.zeros((self.hidden_size, 1))
        c = np.zeros((self.hidden_size, 1))

        for x in inputs:
            x = np.array([[x]])

            combined = np.vstack((h, x))

            # Forget Gate
            f = sigmoid(np.dot(self.Wf, combined) + self.bf)

            # Input Gate
            i = sigmoid(np.dot(self.Wi, combined) + self.bi)

            # Candidate State
            c_bar = tanh(np.dot(self.Wc, combined) + self.bc)

            # Update Cell State
            c = f * c + i * c_bar

            # Output Gate
            o = sigmoid(np.dot(self.Wo, combined) + self.bo)

            # Hidden State
            h = o * tanh(c)

        return h, c


# Give User Input
sequence = list(map(float, input("Enter sequence values separated by space: ").split()))

# Create LSTM
lstm = LSTM(input_size=1, hidden_size=3)

# Run LSTM
hidden_state, cell_state = lstm.forward(sequence)

print("\nFinal Hidden State:")
print(hidden_state)

print("\nFinal Cell State:")
print(cell_state)
#GRU (Gated Recurrent Unit)
#GRU ( is a type of Recurrent Neural Network (RNN) designed to process sequential data and remember important information over time. It was introduced to overcome the vanishing gradient problem of traditional RNNs.

#A GRU uses two gates:

#Update Gate (zₜ): Decides how much past information to keep.
#Reset Gate (rₜ): Decides how much past information to forget.

#Unlike LSTM, GRU does not have a separate cell state, making it simpler and faster.

import numpy as np

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# GRU Class
class GRU:

    def __init__(self):

        # Initialize weights
        self.wz = np.random.rand()
        self.wr = np.random.rand()
        self.wh = np.random.rand()

    def forward(self, sequence):

        h = 0

        for x in sequence:

            # Update Gate Formula 
            z = sigmoid(self.wz * x)

            # Reset Gate Formula
            r = sigmoid(self.wr * x)

            # Candidate Hidden State Formula
            h_candidate = np.tanh(self.wh * (r * x))

            # Update Hidden State Formula
            h = (1 - z) * h + z * h_candidate

        return h


# Take input from user
sequence = list(map(float, input("Enter sequence values: ").split()))

# Create GRU object
gru = GRU()

# Get output
result = gru.forward(sequence)

print("\nFinal Hidden State =", result)
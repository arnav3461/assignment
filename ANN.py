#ANN(Artificial Neural Network)
#An Artificial Neural Network (ANN) is a machine learning model inspired by the working of the
#human brain.
#It consists of interconnected neurons organized into layers that learn patterns from data and 
#make predictions
#ANN layers are:-
#Input Layer
#Hidden Layer(s)
#Output Layer
#----------------
import numpy as np 

# Inputs
X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

# Outputs Using OR GATE
y = np.array([[0],[1],[1],[1]])

# Useing Sigmoid Function
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Derivative
def sigmoid_derivative(x):
    return x*(1-x)

# Initialize Weights
np.random.seed(1)
weights = np.random.rand(2,1)

# ON Training
for epoch in range(5000):

    # Forward Pass
    output = sigmoid(np.dot(X, weights))

    # Error Calculation
    error = y - output

    # Backpropagation Formula
    adjustments = error * sigmoid_derivative(output)

    # Weight Update Formula
    weights += 0.1 * np.dot(X.T, adjustments)

print("Weights:")
print(weights)

# User Input
a = int(input("Enter first value (0 or 1): "))
b = int(input("Enter second value (0 or 1): "))

test = np.array([[a,b]])

prediction = sigmoid(np.dot(test, weights))

print("Prediction:", prediction)
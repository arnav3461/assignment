# ==================================================
# K-NEAREST NEIGHBORS (KNN)

# HOW KNN WORKS
# 1. Choose the value of K.
# 2. Calculate the distance between the new point
# and all the training points.
# 3. Select the K nearest neighbors.
# 4. For classification, use majority voting.
# 5. Assign the class with the highest number of votes.
#=======================================================================
# USER-DEFINED FRUIT CLASSIFICATION

import math


def get_number(message, minimum=None, maximum=None):
    while True:
        try:
            value = float(input(message))

            if minimum is not None and value < minimum:
                print("Value must be at least", minimum)
                continue

            if maximum is not None and value > maximum:
                print("Value must not exceed", maximum)
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Function to accept a valid integer

def get_integer(message, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(message))

            if minimum is not None and value < minimum:
                print("Value must be at least", minimum)
                continue

            if maximum is not None and value > maximum:
                print("Value must not exceed", maximum)
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")



# Function to calculate Euclidean distance
def calculate_distance(point1, point2):
    distance = 0

    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2

    return math.sqrt(distance)


# Function to predict the fruit using KNN
def knn_predict(training_data, test_data, k):
    distances = []

    # Calculate the distance between the new fruit
    # and every fruit in the training dataset
    for item in training_data:
        features = item[0]
        label = item[1]

        distance = calculate_distance(features, test_data)
        distances.append([distance, label, features])

    # Sort the fruits from nearest to farthest
    distances.sort(key=lambda item: item[0])

    # Select the K nearest neighbors
    nearest_neighbors = distances[:k]

    # Count the votes for each fruit
    votes = {}

    for neighbor in nearest_neighbors:
        label = neighbor[1]

        if label in votes:
            votes[label] += 1
        else:
            votes[label] = 1

    # Select the fruit class with the highest votes
    predicted_class = max(votes, key=votes.get)

    return predicted_class, nearest_neighbors, votes

# ENTER TRAINING DATA

print("KNN FRUIT CLASSIFICATION")


number_of_fruits = get_integer(
    "Enter the number of training fruits: ",
    minimum=1
)

training_data = []

print("\nEnter the training fruit information.")

for i in range(number_of_fruits):
    print("\nFruit", i + 1)

    weight = get_number(
        "Enter weight in grams: ",
        minimum=0.01
    )

    sweetness = get_number(
        "Enter sweetness from 1 to 10: ",
        minimum=1,
        maximum=10
    )

    # Ensure that the fruit name is not empty
    while True:
        fruit_name = input("Enter fruit name: ").strip()

        if fruit_name:
            fruit_name = fruit_name.title()
            break

        print("Fruit name cannot be empty.")

    # Store the fruit's features and class
    training_data.append(
        [[weight, sweetness], fruit_name]
    )


# DISPLAY TRAINING DATA

print("TRAINING DATA")


for i, item in enumerate(training_data, start=1):
    features = item[0]
    fruit_name = item[1]

    print(
        i,
        "| Weight:",
        features[0],
        "grams | Sweetness:",
        features[1],
        "| Fruit:",
        fruit_name
    )

# ENTER NEW FRUIT INFORMATION


print("NEW FRUIT INFORMATION")


new_weight = get_number(
    "Enter the new fruit weight in grams: ",
    minimum=0.01
)

new_sweetness = get_number(
    "Enter the new fruit sweetness from 1 to 10: ",
    minimum=1,
    maximum=10
)

new_fruit = [new_weight, new_sweetness]

# ENTER THE VALUE OF K


k = get_integer(
    "Enter the value of K: ",
    minimum=1,
    maximum=len(training_data)
)

# MAKE THE PREDICTION


prediction, neighbors, votes = knn_predict(
    training_data,
    new_fruit,
    k
)

# DISPLAY THE RESULT
print("KNN CLASSIFICATION RESULT")


print("New fruit weight:", new_fruit[0], "grams")
print("New fruit sweetness:", new_fruit[1])
print("Value of K:", k)

print("\nNearest neighbors:")

for neighbor in neighbors:
    distance = neighbor[0]
    label = neighbor[1]
    features = neighbor[2]

    print(
        "Weight:",
        features[0],
        "| Sweetness:",
        features[1],
        "| Fruit:",
        label,
        "| Distance:",
        round(distance, 2)
    )

print("\nVotes:")

for fruit_name, vote_count in votes.items():
    print(fruit_name, ":", vote_count, "vote(s)")

print("\nPredicted fruit:", prediction)
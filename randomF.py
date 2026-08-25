# ==================================================
# RANDOM FOREST CLASSIFICATION 
#Random Forest is a popular machine learning algorithm used for both classification (predicting categories) and regression 
# (predicting numerical values). 
# It works by creating many decision trees and combining their results to produce a more accurate and stable prediction.
# USER-DEFINED FRUIT CLASSIFICATION
# ==================================================


import random
from collections import Counter



# Accept and validate a decimal number

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


# Accept and validate a whole number

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



# Calculate Gini impurity

def calculate_gini(groups):
    total_samples = sum(len(group) for group in groups)

    if total_samples == 0:
        return 0

    gini = 0.0

    for group in groups:
        group_size = len(group)

        if group_size == 0:
            continue

        labels = [row[-1] for row in group]
        label_counts = Counter(labels)

        group_score = 0.0

        for count in label_counts.values():
            probability = count / group_size
            group_score += probability ** 2

        group_gini = 1.0 - group_score

        gini += group_gini * (
            group_size / total_samples
        )

    return gini


# Divide the dataset into left and right groups

def split_data(feature_index, split_value, dataset):
    left_group = []
    right_group = []

    for row in dataset:
        if row[feature_index] < split_value:
            left_group.append(row)
        else:
            right_group.append(row)

    return left_group, right_group


# Find the best feature and value for splitting

def find_best_split(dataset, number_of_features):
    feature_count = len(dataset[0]) - 1

    selected_features = random.sample(
        range(feature_count),
        min(number_of_features, feature_count)
    )

    best_feature = None
    best_value = None
    best_gini = float("inf")
    best_groups = None

    for feature_index in selected_features:
        possible_values = sorted(
            set(row[feature_index] for row in dataset)
        )

        for split_value in possible_values:
            groups = split_data(
                feature_index,
                split_value,
                dataset
            )

            gini = calculate_gini(groups)

            if gini < best_gini:
                best_feature = feature_index
                best_value = split_value
                best_gini = gini
                best_groups = groups

    return {
        "feature": best_feature,
        "value": best_value,
        "gini": best_gini,
        "groups": best_groups
    }

# Find the most common class in a group

def get_majority_class(group):
    labels = [row[-1] for row in group]

    return Counter(labels).most_common(1)[0][0]


# Create the child nodes of a decision tree

def create_children(
    node,
    max_depth,
    minimum_size,
    number_of_features,
    current_depth
):
    left_group, right_group = node["groups"]

    # Remove groups because they are no longer needed
    del node["groups"]

    # If either group is empty, create leaf nodes
    if not left_group or not right_group:
        combined_group = left_group + right_group
        predicted_class = get_majority_class(
            combined_group
        )

        node["left"] = predicted_class
        node["right"] = predicted_class
        return

    # Stop when the maximum tree depth is reached
    if current_depth >= max_depth:
        node["left"] = get_majority_class(
            left_group
        )

        node["right"] = get_majority_class(
            right_group
        )

        return

    # Create the left child
    if len(left_group) <= minimum_size:
        node["left"] = get_majority_class(
            left_group
        )
    else:
        node["left"] = find_best_split(
            left_group,
            number_of_features
        )

        create_children(
            node["left"],
            max_depth,
            minimum_size,
            number_of_features,
            current_depth + 1
        )

    # Create the right child
    if len(right_group) <= minimum_size:
        node["right"] = get_majority_class(
            right_group
        )
    else:
        node["right"] = find_best_split(
            right_group,
            number_of_features
        )

        create_children(
            node["right"],
            max_depth,
            minimum_size,
            number_of_features,
            current_depth + 1
        )

# Build one decision tree

def build_tree(
    training_sample,
    max_depth,
    minimum_size,
    number_of_features
):
    root = find_best_split(
        training_sample,
        number_of_features
    )

    create_children(
        root,
        max_depth,
        minimum_size,
        number_of_features,
        1
    )

    return root



# Create a bootstrap sample

def create_bootstrap_sample(dataset):
    sample = []

    for _ in range(len(dataset)):
        random_row = random.choice(dataset)
        sample.append(random_row)

    return sample

# Predict a class using one decision tree
def predict_with_tree(node, test_fruit):
    feature_index = node["feature"]
    split_value = node["value"]

    if test_fruit[feature_index] < split_value:
        if isinstance(node["left"], dict):
            return predict_with_tree(
                node["left"],
                test_fruit
            )

        return node["left"]

    if isinstance(node["right"], dict):
        return predict_with_tree(
            node["right"],
            test_fruit
        )

    return node["right"]

# Build multiple decision trees

def build_random_forest(
    dataset,
    number_of_trees,
    max_depth,
    minimum_size,
    number_of_features
):
    forest = []

    for _ in range(number_of_trees):
        bootstrap_sample = create_bootstrap_sample(
            dataset
        )

        tree = build_tree(
            bootstrap_sample,
            max_depth,
            minimum_size,
            number_of_features
        )

        forest.append(tree)

    return forest


# Predict using all decision trees

def random_forest_predict(forest, test_fruit):
    tree_predictions = []

    for tree in forest:
        prediction = predict_with_tree(
            tree,
            test_fruit
        )

        tree_predictions.append(prediction)

    vote_counts = Counter(tree_predictions)

    final_prediction = vote_counts.most_common(1)[0][0]

    return final_prediction, tree_predictions, vote_counts

# START THE PROGRAM



print("RANDOM FOREST FRUIT CLASSIFICATION")


# Keep the random result consistent each time
random.seed(42)


# ACCEPT TRAINING DATA FROM THE USER


number_of_fruits = get_integer(
    "Enter the number of training fruits: ",
    minimum=2
)

training_data = []

print("\nEnter the training fruit information.")
print("Use at least two fruit classes.")
print("Examples: Apple, Orange, Grapes\n")

for i in range(number_of_fruits):
    print("Fruit", i + 1)

    weight = get_number(
        "Enter weight in grams: ",
        minimum=0.01
    )

    sweetness = get_number(
        "Enter sweetness from 1 to 10: ",
        minimum=1,
        maximum=10
    )

    while True:
        fruit_name = input(
            "Enter fruit name: "
        ).strip()

        if fruit_name:
            fruit_name = fruit_name.title()
            break

        print("Fruit name cannot be empty.")

    # Format:
    # [weight, sweetness, class name]
    training_data.append(
        [weight, sweetness, fruit_name]
    )

    print()



# CHECK THE NUMBER OF CLASSES


fruit_classes = set(
    row[-1] for row in training_data
)

if len(fruit_classes) < 2:
    print("\nThe dataset has only one fruit class.")
    print("Classification requires at least two classes.")
    print("Please run the program again.")
    raise SystemExit



# DISPLAY THE TRAINING DATA



print("TRAINING DATA")


for index, row in enumerate(
    training_data,
    start=1
):
    print(
        index,
        "| Weight:",
        row[0],
        "grams | Sweetness:",
        row[1],
        "| Fruit:",
        row[2]
    )

# ACCEPT THE NEW FRUIT INFORMATION



print("NEW FRUIT INFORMATION")

new_weight = get_number(
    "Enter new fruit weight in grams: ",
    minimum=0.01
)

new_sweetness = get_number(
    "Enter new fruit sweetness from 1 to 10: ",
    minimum=1,
    maximum=10
)

new_fruit = [
    new_weight,
    new_sweetness
]



# ACCEPT RANDOM FOREST SETTINGS


print("RANDOM FOREST SETTINGS")


number_of_trees = get_integer(
    "Enter the number of trees: ",
    minimum=1
)

max_depth = get_integer(
    "Enter the maximum depth of each tree: ",
    minimum=1
)

minimum_size = get_integer(
    "Enter the minimum leaf size: ",
    minimum=1
)

# This dataset has two features:
# Feature 0: Weight
# Feature 1: Sweetness

number_of_features = get_integer(
    "Enter random features per split, 1 or 2: ",
    minimum=1,
    maximum=2
)

# BUILD THE RANDOM FOREST


forest = build_random_forest(
    training_data,
    number_of_trees,
    max_depth,
    minimum_size,
    number_of_features
)

# MAKE THE FINAL PREDICTION


prediction, tree_predictions, votes = (
    random_forest_predict(
        forest,
        new_fruit
    )
)

# DISPLAY THE RESULTS


print("RANDOM FOREST CLASSIFICATION RESULT")


print(
    "New fruit weight:",
    new_fruit[0],
    "grams"
)

print(
    "New fruit sweetness:",
    new_fruit[1]
)

print(
    "Number of trees:",
    number_of_trees
)

print(
    "Maximum tree depth:",
    max_depth
)

print("\nPrediction from each tree:")

for index, tree_prediction in enumerate(
    tree_predictions,
    start=1
):
    print(
        "Tree",
        index,
        "predicted:",
        tree_prediction
    )

print("\nRandom Forest votes:")

for fruit_name, vote_count in votes.items():
    print(
        fruit_name,
        ":",
        vote_count,
        "vote(s)"
    )

print("\nFinal predicted fruit:", prediction)
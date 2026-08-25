#XGBoost Definition

#XGBoost (eXtreme Gradient Boosting) is a powerful supervised machine learning algorithm 
#that uses gradient boosting to build multiple decision trees and combine them to make highly accurate predictions.
#Employee Salary Prediction
from xgboost import XGBRegressor

# Number of records
n = int(input("Enter number of employees: "))

X = []
y = []

# User enters training data
for i in range(n):
    experience = float(input(f"\nEmployee {i+1} Experience (years): "))
    salary = float(input(f"Employee {i+1} Salary: "))

    X.append([experience])
    y.append(salary)

# Create and train model
model = XGBRegressor(
    n_estimators=50,
    learning_rate=0.1,
    max_depth=3,
    objective="reg:squarederror",
    random_state=42
)

model.fit(X, y)

# New prediction
new_exp = float(input("\nEnter experience to predict salary: "))

prediction = model.predict([[new_exp]])

print("\nPredicted Salary =", round(float(prediction[0]), 2))
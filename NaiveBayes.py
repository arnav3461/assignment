#Naive Bayes
#Naive Bayes is a supervised machine learning algorithm used mainly for classification problems.
#It is based on Bayes' Theorem and assumes that all input features are independent of each other.
#P(A∣B)=P(B∣A)×P(A)​/p(B)
#Student Result Prediction
from sklearn.naive_bayes import GaussianNB

n = int(input("Enter number of students: "))

X = []
y = []


for i in range(n):
    hours = float(input(f"\nStudent {i+1} Study Hours: "))
    result = int(input("Pass(1) or Fail(0): "))

    X.append([hours])
    y.append(result)

# Train model
model = GaussianNB()
model.fit(X, y)

# Prediction
test_hours = float(input("\nEnter study hours to predict: "))

prediction = model.predict([[test_hours]])

if prediction[0] == 1:
    print("Predicted Result: PASS")
else:
    print("Predicted Result: FAIL")
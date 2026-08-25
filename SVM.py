#SVM (Support Vector Machine) Definition

#Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression. It works
#by finding the best boundary (hyperplane) that separates data points of different classes with the maximum margin.

#Pass Students    |     Fail Students

#     ● ● ●       |      ○ ○ ○
#     ● ● ●       |      ○ ○ ○

#-------------------------------
#    Best Separating Boundary
#===============================


from sklearn.svm import SVC

n = int(input("Enter number of students: "))

X = []
y = []

for i in range(n):
    print(f"\nStudent {i+1}")

    hours = float(input("Study Hours: "))
    attendance = float(input("Attendance %: "))
    result = int(input("Pass(1) or Fail(0): "))

    X.append([hours, attendance])
    y.append(result)

# Train SVM
#============
model = SVC(kernel="linear")
model.fit(X, y)

print("\nEnter details for prediction")

hours = float(input("Study Hours: "))
attendance = float(input("Attendance %: "))

prediction = model.predict([[hours, attendance]])

if prediction[0] == 1:
    print("Predicted Result: PASS")
else:
    print("Predicted Result: FAIL")

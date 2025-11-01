# 1️⃣ Import libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

print("Name : Aryan Rana \nRoll No : 1323223")
# 2️⃣ Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

print("Dataset shape:", df.shape)
print(df.head())

# 3️⃣ Split features and target
X = df.drop('target', axis=1)
y = df['target']

# 4️⃣ Train-test split (70:30)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 5️⃣ Initialize and train Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 6️⃣ Make predictions
y_pred = model.predict(X_test)

# 7️⃣ Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\n✅ Model Accuracy: {accuracy:.4f}")

# 8️⃣ Detailed classification metrics
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 9️⃣ Confusion Matrix visualization
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Decision Tree on Iris")
plt.show()

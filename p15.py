# 1️⃣ Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from lazypredict.Supervised import LazyClassifier

print("Name : Aryan Rana \nRoll No : 1323223")

# 2️⃣ Load the dataset
df = pd.read_csv("diabetes.csv")  # <-- ensure data.csv is in the same folder
print("Dataset shape:", df.shape)
print(df.head())

# 3️⃣ Data Cleaning
# Check for missing values
print("\nMissing values before cleaning:\n", df.isnull().sum())

# Replace 0 with NaN in certain medical features (invalid values)
cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols_with_zero] = df[cols_with_zero].replace(0, np.nan)

# Fill missing with median values
df.fillna(df.median(), inplace=True)

print("\nMissing values after cleaning:\n", df.isnull().sum())

# 4️⃣ Correlation Visualization
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation - Pima Indians Diabetes Dataset")
plt.suptitle("Aryan Rana", fontsize=12, fontweight='bold')
plt.show()

# 5️⃣ Split dataset (70:30)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 6️⃣ Train Random Forest Classifier
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# 7️⃣ Evaluate Random Forest
accuracy = accuracy_score(y_test, y_pred)
print(f"\n✅ Random Forest Accuracy: {accuracy:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 8️⃣ Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.suptitle("Aryan Rana", fontsize=12, fontweight='bold')
plt.title('Confusion Matrix - Random Forest')
plt.show()


# 9️⃣ Compare all models using LazyPredict
clf = LazyClassifier(verbose=0, ignore_warnings=True, custom_metric=None)
models, predictions = clf.fit(X_train, X_test, y_train, y_test)

print("\nModel Comparison Results:\n")
print(models.head(10))  # Show top 10 models

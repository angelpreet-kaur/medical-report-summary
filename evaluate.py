import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# Read CSV file
df = pd.read_csv("evaluation.csv")

# Actual and Predicted values
y_true = df["Actual"]
y_pred = df["Predicted"]

# Metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("=" * 40)
print("MODEL EVALUATION RESULTS")
print("=" * 40)

print(f"Accuracy  : {accuracy:.2f}")
print(f"Precision : {precision:.2f}")
print(f"Recall    : {recall:.2f}")
print(f"F1 Score  : {f1:.2f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_true, y_pred))
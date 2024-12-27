from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import pickle

# Load dataset
data = load_iris(as_frame=True)
X = data.data
y = data.target

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model building
model = LogisticRegression()
model.fit(x_train, y_train)

# Predictions
y_pred = model.predict(x_test)

# Evaluation metrics
accuracy = accuracy_score(y_pred, y_test)
precision = precision_score(y_pred, y_test, average='weighted')
recall = recall_score(y_pred, y_test, average='weighted')
f1 = f1_score(y_pred, y_test, average='weighted')
cm = confusion_matrix(y_pred, y_test)

# Print results
print(f'Confusion Matrix:\n{cm}')
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')

# save model
pickle.dump(model, open('model.pkl', 'wb'))

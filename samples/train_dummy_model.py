import numpy as np
from sklearn import svm
import joblib

# Dummy features for rock, paper, scissors
X = np.array([
    [0, 0, 1],  # rock
    [1, 1, 1],  # paper
    [0, 1, 0],  # scissors
])
y = ['rock', 'paper', 'scissor']

# Train model
clf = svm.SVC()
clf.fit(X, y)
       
# Save to file
joblib.dump(clf, 'gesture_model.pkl')
print("✅ Model trained and saved as 'gesture_model.pkl'")

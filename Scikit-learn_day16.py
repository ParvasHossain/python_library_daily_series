from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample feature matrix
X = np.array([[1.0, 20.0], [2.0, 30.0], [3.0, 10.0]])
y = np.array([0, 1, 0])

# Modular pipeline enforcing consistent fit/transform contracts
model_pipeline = Pipeline([
    ('scaler', StandardScaler()),       # Transformer: fit() + transform()
    ('classifier', LogisticRegression()) # Predictor: fit() + predict()
])

# Single fit contract triggers unified sequence execution
model_pipeline.fit(X, y)
print("Pipeline Predictions:", model_pipeline.predict(X))
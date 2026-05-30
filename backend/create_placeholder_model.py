import joblib
from sklearn.dummy import DummyRegressor
import numpy as np

# Create a dummy model that just predicts the mean value 
# (this is just to have a valid .pkl file as requested)

X = np.array([[1], [2], [3], [4]])
y = np.array([50, 100, 150, 200])

dummy_model = DummyRegressor(strategy="mean")
dummy_model.fit(X, y)

joblib.dump(dummy_model, "model.pkl")
print("Placeholder model.pkl created successfully.")

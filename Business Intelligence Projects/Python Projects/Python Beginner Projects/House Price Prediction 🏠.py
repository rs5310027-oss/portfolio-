import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    "Area": [1000, 1500, 2000, 2500, 3000],
    "Price": [200000, 300000, 400000, 500000, 600000]
}

df = pd.DataFrame(data)

# Input (X) and Output (y)
X = df[["Area"]]
y = df["Price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
new_area = [[1800]]
prediction = model.predict(new_area)

print("Predicted House Price:", prediction[0])
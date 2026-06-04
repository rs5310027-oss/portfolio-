from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dataset
messages = [
    "Win money now",
    "Hello how are you",
    "Claim your free prize",
    "Let's meet tomorrow"
]

labels = ["spam", "ham", "spam", "ham"]

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Test message
test = ["Free money available"]
test_vector = vectorizer.transform(test)

prediction = model.predict(test_vector)

print("Prediction:", prediction[0])
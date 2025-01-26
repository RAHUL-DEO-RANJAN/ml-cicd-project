from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
import os

# Flask app
app = Flask(__name__)

# Helper function to load dataset
def load_data():
    from sklearn.datasets import load_iris
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df


def train_model():
    """
    Train a Random Forest Classifier on the Iris dataset.
    Returns:
    float: Accuracy of the model on the test set.
    """
    print("Training the model...")
    data = load_data()
    X = data.iloc[:, :-1]
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Data Preprocessing
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train Model
    classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    classifier.fit(X_train, y_train)

    # Save Model and Scaler
    joblib.dump(classifier, 'random_forest_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    print("Model and scaler saved successfully!")
    return data, X, y, X_train, X_test, y_train, y_test

# Check if the model file exists, if not, train and save it
if not os.path.exists('random_forest_model.pkl') or not os.path.exists('scaler.pkl'):
    data, X, y, X_train, X_test, y_train, y_test = train_model()
else:
    print("Loading existing model and scaler...")
    data = load_data()
    X = data.iloc[:, :-1]
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    scaler = joblib.load('scaler.pkl')


if __name__ == "__main__":
    accuracy = train_model()

   
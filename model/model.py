from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_model():
    """
    Train a Random Forest Classifier on the Iris dataset.

    Returns:
        float: Accuracy of the model on the test set.
    """
    # Load iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy
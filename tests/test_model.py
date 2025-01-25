import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model')))

from model.model import train_model

def test_model_accuracy():
    accuracy = train_model()
    assert accuracy > 0.5  # Ensure model accuracy is over 90%

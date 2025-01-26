from model.model import train_model
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model')))

def test_model_accuracy():
    accuracy = train_model()
    assert accuracy > 0.2
    
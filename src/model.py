from src.data_validation import validate_experience
from pathlib import Path
import joblib 

BASE_DIR=Path(__file__).resolve().parent.parent 
MODEL_PATH=BASE_DIR/"models"/"salary_model.joblib"

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model not found"
        )
    return joblib.load(MODEL_PATH)

def predict_salary(experience):
    validate_experience(experience)
    model=load_model()
    prediction=model.predict([[experience]])
    return float(prediction[0])
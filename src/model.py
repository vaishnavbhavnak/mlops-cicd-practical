from src.data_validation import validate_experience

def predict_salary(experience):
    validate_experience(experience)
    
    salary=20000+(experience*5000)
    return salary 
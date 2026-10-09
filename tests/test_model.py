import pytest
from src.model import predict_salary,load_model
from src.data_validation import validate_experience

def test_salary_prediction():
    result=predict_salary(3)
    assert result==pytest.approx(35000,abs=1)
    
def test_zero_exerience():
    result=predict_salary(0)
    assert result==pytest.approx(20000,abs=1)
    
def test_negative_exerience():
    with pytest.raises(ValueError):
        predict_salary(-1)
        
def test_valid_string_input():
    with pytest.raises(TypeError):
        predict_salary("five")
        
def test_negative_experience_validation():
    with pytest.raises(ValueError):
        validate_experience(-2)
        
def test_valid_experience():
    assert validate_experience(5) is True
    
def test_model_loads():
    model=load_model()
    assert model is not None 
    

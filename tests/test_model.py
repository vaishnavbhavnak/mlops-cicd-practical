import pytest
from src.model import predict_salary

def test_salary_prediction():
    result=predict_salary(3)
    assert result==35000
    
def test_zero_exerience():
    result=predict_salary(0)
    assert result==20000
    
def test_negative_exerience():
    with pytest.raises(ValueError):
        predict_salary(-1)
        
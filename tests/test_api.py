from fastapi .testclient import TestClient
from src.main import app

client=TestClient(app)

def test_home_endpoint():
    response=client.get("/")
    
    assert response.status_code == 200 
    assert response.json()["message"]==(
        "ML Salary Prediction API is running"
    )
    
def test_health_endpoint():
    response=client.get("/health")
    
    assert response.status_code == 200 
    assert response.json()["status"]== "healthy"
    
def test_prediction_endpoint():
    response= client.post(
        "/predict",
        json={"experience":3}
    )
    assert response.status_code == 200
    assert response.json()["predicted_salary"] == 35000.0
    
def test_negative_experience_rejected():
    response= client.post(
        "/predict",
        json={"experience":-3}
    )
    assert response.status_code == 422

def test_string_experience_rejected():
    response= client.post(
        "/predict",
        json={"experience":"five"}
    )
    assert response.status_code == 422

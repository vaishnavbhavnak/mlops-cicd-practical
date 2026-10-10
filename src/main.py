from fastapi import FastAPI,HTTPException
from pydantic import BaseModel , Field

from src.model import predict_salary

app=FastAPI(title="ML Salary Prediction API")

class PredictionRequest(BaseModel):
    experience: float = Field(ge=0,le=50)
    
class PredictionResponse(BaseModel):
    experience: float 
    predicted_salary : float 
    
@app.get("/")
def home():
    return {"message":"ML Salary Prediction API is running"}

@app.get("/health")
def health():
    return {"status":"healthy"}

@app.post("/predict",response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        salary=predict_salary(request.experience)
        
        return {
            "experience": request.experience, 
            "predicted_salary":salary
        }
    except (ValueError,TypeError) as error :
        raise HTTPException(status_code=400, detail=str(error)) from error 
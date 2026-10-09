from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

BASE_DIR=Path(__file__).resolve().parent.parent 
MODEL_DIR=BASE_DIR/"models"
MODEL_PATH=MODEL_DIR/"salary_model.joblib"

def train_model():
    X=np.array([[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
    y=np.array([20000,25000,30000,35000,40000,45000,50000,55000,60000,65000,70000])
    
    model=LinearRegression()
    model.fit(X,y)
    
    MODEL_DIR.mkdir(parents=True,exist_ok=True)
    joblib.dump(model,MODEL_PATH)
    
    print(f"Model saved to: {MODEL_PATH}")
    
if __name__=="__main__":
    train_model()
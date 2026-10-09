def predict_salary(experience):
    if experience<0:
        raise ValueError("Experience cannot be negative")
    
    salary=20000+(experience*5000)
    return salary 
def validate_experience(experience):
    if not isinstance(experience,(int,float)):
        raise TypeError("Experience must be a number")
    
    if experience < 0:
        raise ValueError("Experience cannot be negative")
    
    return True
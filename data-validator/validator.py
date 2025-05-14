def validate_string(value, field_name="Value"):
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")
    return value

def validate_float(value, field_name="Value"):
    try:
        value = float(value)
    except (ValueError, TypeError):
        raise TypeError(f"{field_name} must be a float")
    if value < 0:
        raise ValueError(f"{field_name} must be positive") 
    return value

def validate_int(value, field_name="Value"):
    try:
        value = int(value)
    except (ValueError, TypeError):
        raise TypeError(f"{field_name} must be an integer")
    if value < 0:
        raise ValueError(f"{field_name} must be positive")
    return value

def validate_discount(value, field_name="Discount"):
    try:
        value = float(value)
    except (ValueError, TypeError):
        raise TypeError(f"{field_name} must be a float")
    
    if not (0 < value <= 100):
        raise ValueError(f"{field_name} must be greater than 0 and less than or equal to 100")
    
    return value

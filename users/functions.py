import re

def password_requirements(password: str) -> str | None:
    """
    Function responsible for checking if the minimum password requirements are being respected.

    Params:
        password [str]: password that will be checked
    
    Returns:
        Error message [str] or None
    """

    minimal_number_char = 1
    minimal_upper_char = 1
    minimal_lower_char = 1
    minimal_special_char = 1
    minimal_length = 8

    if len(re.findall(r'[A-Z]', password)) < minimal_upper_char:
        return f'Password must be at least {minimal_upper_char} uppercase character(s)!'
    
    if len(re.findall(r'[a-z]', password)) < minimal_lower_char:
        return f'Password must be at least {minimal_lower_char} lowercase character(s)!'
    
    if len(re.findall(r'[0-9]', password)) < minimal_number_char:
        return f'Password must be at least {minimal_number_char} number(s)!'
    
    if len(re.findall(r'[^\w\s]', password)) < minimal_special_char:
        return f'Password must be at least {minimal_special_char} special character(s)!'
    
    if len(password or ()) < minimal_length:
        return f'Password must be at least {minimal_length} characters!'
    
    return None
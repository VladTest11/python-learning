def convert_temperature(temp, unit):
    """
    Convert temperature between Celsius and Fahrenheit.
    
    Args:
        temp: Temperature value (numeric)
        unit: 'C' for Celsius or 'F' for Fahrenheit
        
    Returns:
        float: Converted temperature rounded to 2 decimal places
        
    Raises:
        ValueError: If unit is not 'C' or 'F'
    """
    # Input validation and normalization
    temp = float(temp)  # Accepts int(32) or float(32.5) or even string("32")
    unit = str(unit).upper()    # Case-insensitive: 'c', 'C', 'f', 'F' all work
    
    # Conversion logic
    if unit == 'C':
        # Celsius to Fahrenheit: F = (C × 9/5) + 32
        result = (temp * 9/5) + 32
    elif unit == 'F':
        # Fahrenheit to Celsius: C = (F - 32) × 5/9
        result = (temp - 32) * 5/9
    else:
        # Raise exception for invalid input
        raise ValueError(f"Invalid unit '{unit}'. Must be 'C' or 'F'.")
    
    # Round to 2 decimal places as per requirements
    return round(result, 2)

if __name__ == "__main__":
    # Test cases    
    print(convert_temperature(0, 'c'))
    print(convert_temperature(32, 'f'))
    print(convert_temperature(100, 'C'))
    print(convert_temperature(98.6, 'F'))

    # Test error handling
    try:
        print(convert_temperature(100, 'K'))  # Should raise ValueError
    except ValueError as e:
        print(f"Caught error: {e}")
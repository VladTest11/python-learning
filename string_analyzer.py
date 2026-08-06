def analyze_string(text):
    """
    Analyze the input string and return various statistics.
    
    Args:
        text: Input string to be analyzed.

    Returns:
        dict: A dictionary containing:
            - 'char_count': Total characters including spaces
            - 'word_count': Total words (space-separated)
            - 'most_frequent_char': Most common character (excluding spaces)
                                   Returns None if no valid characters are present.
    """
    text = str(text)  # Ensure input is treated as a string
    char_count = len(text)  # Count of characters including spaces
    word_count = len(text.split())  # Count of words split on any whitespace character (including \n \r \t \f and spaces) 
    text_lower = text.lower() # Normalize to lowercase for frequency analysis
    
    char_freq = {}  # Dictionary to hold character frequencies
    for char in text_lower:
        # Iterate through each character to build frequency dictionary and ignore spaces
        if char != ' ':
            char_freq[char] = char_freq.get(char, 0) + 1
            #   IMPORTANT!: This pythonic(!) pattern appears everywhere in data processing, log analysis, word counting, etc.
    
    # Determine the most frequent character
    if char_freq:
        most_frequent = max(char_freq, key=char_freq.get)
        # max() normally finds largest number
        # key= parameter lets you specify HOW to compare
        # char_freq.get means "compare by dictionary values"
    else:
        most_frequent = None  # No valid characters present

    return {
        'char_count': char_count,
        'word_count': word_count,
        'most_frequent_char': most_frequent
    }

if __name__ == "__main__":
    # Test cases:
    # Should return dictionary with character count, word count, and most frequent character
    print(analyze_string("Hello World! Hello Universe!"))
    print(analyze_string("Python is awesome"))
    print(analyze_string("   "))
    print(analyze_string(""))
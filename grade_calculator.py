"""
Grade Calculator

This provides functions to calculate letter grades from numeric scores,
compute statistics on a list of scores, and process grades to return both letter
grades and statistics.

Functions:
- calculate_letter_grade(score): Convert numeric score to letter grade
- calculate_statistics(scores): Calculate statistics for a list of scores
- process_grades(scores): Process scores to return grades and statistics
"""
def calculate_letter_grade(score):
    """
    Calculate the letter grade for a given numeric score.
    
    Args:
        score: Numeric score (0-100)
        
    Returns:
        str: Letter grade ('A', 'B', 'C', 'D', 'F') or 'Invalid score'
    """
    if not isinstance(score, (int, float)) or score > 100 or score < 0:  # Handle invalid input (guard clause)
        return "Invalid score"
    elif score >= 90 and score <= 100:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else: 
        return "F"

def calculate_statistics(scores):
    """
    Calculate statistics for a list of numeric scores.
    
    Args:
        scores: List of numeric scores
        
    Returns:
        dict: Statistics with keys 'average', 'highest', 'lowest', 'pass_rate'
              Returns None if scores is empty or invalid
    """
    # Type validation
    if not scores or not isinstance(scores, list): 
        return None
    
    # Check all elements are numbers
    if not all(isinstance(score, (int, float)) for score in scores):
        return None
    
    # Check all scores are in valid range
    if not all(0 <= score <= 100 for score in scores):
        return None
    
    # Calculate basic statistics
    average = round(sum(scores) / len(scores), 1)
    highest = max(scores)
    lowest = min(scores)
    
    # Count passing scores
    passing = 0
    for score in scores: # The Accumulator Pattern (Counting)
        if score >= 60 and score <= 100:
            passing += 1
    
    # Calculate pass rate as percentage
    pass_rate = (passing / len(scores)) * 100
    
    return {
        'average': average,
        'highest': highest,
        'lowest': lowest,
        'pass_rate': pass_rate
    }

def process_grades(scores):
    """
    Process a list of numeric scores to get letter grades and statistics.
    
    Args:
        scores: List of numeric scores
        
    Returns:
        dict: Dictionary with 'grades' (list of letter grades) and 
              'statistics' (dict from calculate_statistics)
    """
    letter_grades = [calculate_letter_grade(score) for score in scores]
    statistics = calculate_statistics(scores)
    
    return {
        'grades': letter_grades, 
        'statistics': statistics
    }

# Comprehensive testing
if __name__ == "__main__":  # Only run tests when script is executed directly
    print("=" * 50)
    print("TESTING LETTER GRADES")
    print("=" * 50)
    
    test_scores_individual = [95, 85, 75, 65, 55, 105, -5]
    expected = ['A', 'B', 'C', 'D', 'F', 'Invalid score', 'Invalid score']
    
    for score, exp in zip(test_scores_individual, expected):
        result = calculate_letter_grade(score)
        status = "✓" if result == exp else "✗"
        print(f"{status} Score {score:3}: {result:15} (expected: {exp})")
    
    print("\n" + "=" * 50)
    print("TESTING STATISTICS")
    print("=" * 50)
    
    test_cases = [
        ([85, 92, 78, 90, 88], {'average': 86.6, 'highest': 92, 'lowest': 78, 'pass_rate': 100.0}),
        ([92, 85, 78, 90, 88, 76, 95, 82], {'average': 85.8, 'highest': 95, 'lowest': 76, 'pass_rate': 100.0}),
        ([100, 0, 50, 60], {'average': 52.5, 'highest': 100, 'lowest': 0, 'pass_rate': 50.0}),
        ([], None),
    ]
    
    for scores, expected in test_cases:
        result = calculate_statistics(scores)
        status = "✓" if result == expected else "✗"
        print(f"{status} Scores {scores}")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}\n")
    
    print("=" * 50)
    print("TESTING PROCESS_GRADES")
    print("=" * 50)
    
    test_scores = [85, 92, 78, 90, 88]
    result = process_grades(test_scores)
    print(f"Scores: {test_scores}")
    print(f"Grades: {result['grades']}")
    print(f"Stats: {result['statistics']}")
    
    # Example usage:
    # print("============================")
    # print("Testing grade A:")
    # print(calculate_letter_grade(95))   # 'A'
    # print("============================")
    # print("Testing grade B:")
    # print(calculate_letter_grade(82))   # 'B'
    # print("============================")
    # print("Testing grade C:")
    # print(calculate_letter_grade(75))   # 'C'
    # print("============================")
    # print("Testing grade D:")
    # print(calculate_letter_grade(65))   # 'D'
    # print("============================")
    # print("Testing grade F:")
    # print(calculate_letter_grade(55))   # 'F'
    # print("============================")
    # print("Testing invalid scores:")
    # print("Score higher than 100:")
    # print(calculate_letter_grade(105))   # 'Invalid score'
    # print("Score lower than 0:")
    # print(calculate_letter_grade(-5))   # 'Invalid score'
    # print("Non-numeric score:")
    # print(calculate_letter_grade("A+"))   # 'Invalid score'
    # print("============================")
    # print("Testing statistics calculation:")
    # print("Test scores: [85, 92, 78, 90, 88]")
    # test_scores = [85, 92, 78, 90, 88]
    # print(calculate_statistics(test_scores))  # {'average': 86.6, 'highest': 92, 'lowest': 78, 'pass_rate': 100.0}
    # print("============================")
    # print("Test scores: [92, 85, 78, 90, 88, 76, 95, 82]")
    # test_scores = [92, 85, 78, 90, 88, 76, 95, 82] # {'average': 85.8, 'highest': 95, 'lowest': 76, 'pass_rate': 100.0}
    # print(calculate_statistics(test_scores))
    # print("============================")
    # # Test edge cases
    # print("Test scores: [] (empty list)")
    # empty_scores = []
    # print(calculate_statistics(empty_scores))  # None
    # print("============================")
    # print("Test scores: [100, 0, 50, 60]")
    # print(process_grades([100, 0, 50, 60])) # ({'grades': ['A', 'F', 'F', 'D'], 'statistics': {'average': 52.5, 'highest': 100, 'lowest': 0, 'pass_rate': 50.0}})
    # print("============================")
    # print("Test scores: string input (invalid)")
    # invalid_scores = "85, 92, 78"
    # print(calculate_statistics(invalid_scores))  # None
    # print("============================")
    # print("Test scores: string list (invalid)")
    # string_list_scores = ["85", "92", "78"]
    # print(calculate_statistics(string_list_scores))  # None
    # print("============================")
    # print("Testing process_grades function:")
    # print("Test scores: [85, 92, 78, 90, 88]")
    # test_scores = [85, 92, 78, 90, 88]
    # print(process_grades(test_scores))  # (['B', 'A', 'C', 'A', 'B'], {'average': 86.6, 'highest': 92, 'lowest': 78, 'pass_rate': 100.0})
    # print("============================")
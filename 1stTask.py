# -- TASK 1 -- #

# Define task variables, give them values
n = "vienas du trys"
a = "vn "
b = "ayds"

def calculate_text_score(text, negative_chars, positive_chars):
    # Check that all inputs are strings
    if not isinstance(text, str) or not isinstance(positive_chars, str) or not isinstance(negative_chars, str):
        raise TypeError("All inputs must be strings")
    
    # Check that all inputs are non-empty
    if len(text) == 0 or len(positive_chars) == 0 or len(negative_chars) == 0:
        raise ValueError("All inputs must be non-empty")
    
    # Initialize score to 0
    score = 0
    
    # Loop through each character in n
    for c in text:
        # If the character is in a (positive chars), increment score
        if c in positive_chars:
            score += 1
        # If the character is in b (negative chars), decrease score
        elif c in negative_chars:
            score -= 1
    
    # Return the calculated score
    print(score)

# Execute the function
calculate_text_score(n, a, b)
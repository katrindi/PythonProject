# -- TASK 1 -- #

# Assign input values to variables using tuple unpacking
n, a, b = input("Enter full text, text with positive characters, and text with negative characters separated by commas: ").split(",")

def calculate_text_score(text, positive_chars, negative_chars):
    # Check that all inputs are strings
    if not isinstance(n, str) or not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("All inputs must be strings")
    
    # Check that all inputs are non-empty
    if len(n) == 0 or len(a) == 0 or len(b) == 0:
        raise ValueError("All inputs must be non-empty")
    
    # Initialize score to 0
    score = 0
    
    # Loop through each character in n
    for c in n:
        # If the character is in a, increment score
        if c in a:
            score += 1
        # If the character is in b, decrement score
        elif c in b:
            score -= 1
    
    # Return the calculated score
    print(score)

# Execute the function
calculate_text_score(n, a, b)
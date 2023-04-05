# -- TASK 1 -- #
# Define default variables, give them values
n = "vienas du trys"
a = "vn "
b = "ayds"

# ERROR HANDLING #

# [1] Checking whether all inputs are strings
if not isinstance(n, str) or not isinstance(a, str) or not isinstance(b, str):
    raise TypeError("All inputs must be strings")

# [2] Checking whether input string is empty
if len(n) == 0:
    raise TypeError("Input string cannot be empty")

# Score function which will calculate the total score
def calculate_text_score(text, positive_chars, negative_chars):
    # Define the initializing score as 0
    score = 0
    # Going through full text variable
    for char in text:
        # If CHAR is in positive CHARS, increase score
        if char in positive_chars:
            score += 1
        # If CHAR is in negative CHARS, decrease score
        elif char in negative_chars:
            score -= 1

    # Print the final score
    print(score)

# Calling function with n,a,b values
calculate_text_score(n, a, b)


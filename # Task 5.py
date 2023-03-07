# Task 5

# Function which will calculate the score
def cal_repetitions(a):
    # Define values by default
    first_char = ""
    new_string = ""
    num_repetitions = 0
    # Check each character in x string
    for char in a:
        if char != first_char:
            # Add the previous character and its count to the new string
            if num_repetitions > 0:
                new_string += str(num_repetitions)
            # Add the new character to the new string
            new_string += char
            # Define first_char value as char
            first_char = char
            # Reset the count of repetitions
            num_repetitions = 1
        else:
            # Increment the count of repetitions
            num_repetitions += 1
    # If the current character is the last one
    if char == a[-1]:
        # Add the count of the last character to the new string
        new_string += str(num_repetitions)
    print(new_string)
    
x = "aabccd"
# Calling function with input string x
cal_repetitions(x)
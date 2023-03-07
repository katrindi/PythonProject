# -- TASK 5 -- #

# Assign input value to a variable
x = input("Enter a string: ")

def compress_text(x):
    # Check if the input is a string
    if not isinstance(x, str):
        raise TypeError("Input must be a string")
    
    # Check if the input string is empty
    if len(x) == 0:
        return ""
    
    # Initialize variables for the current character and its count
    compressed_text = ""
    current_char = x[0]
    current_count = 1
    
    # Loop over the rest of the characters in the input string
    for i in range(1, len(x)):
        # If the current character is the same as the previous character,
        # increment the count
        if x[i] == current_char:
            current_count += 1
        # If the current character is different from the previous character,
        # add the compressed version of the previous character and count to the
        # output string, reset the current character and count to the current
        # character and a count of 1
        else:
            compressed_text += current_char + str(current_count)
            current_char = x[i]
            current_count = 1
    
    # Add the compressed version of the last character and count to the output
    # string
    compressed_text += current_char + str(current_count)

    # Return compressed output string
    return compressed_text
    
# Calling function, providing params
compressed = compress_text(x)

# Returning compressed string value
print(compressed)

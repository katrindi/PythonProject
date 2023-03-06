# -- TASK 5 -- #
# Function Definition
def compress_text(x):

    # ERROR HANDLING #

    # [1] Checking whether input is a string
    if not isinstance(x, str):
        raise TypeError("Input must be a string")
    
    # [2] Checking whether input string is empty
    if len(x) == 0:
        raise TypeError("Input string cannot be empty")

    # "compressed" variable, which will contain the compressed output string
    compressed = ""

    # Current character in text
    current_char = x[0]

    # The count of this character (starts at 1, because already found)
    count = 1
    
    # Loop goes through the full intial text
    for i in range(1, len(x)):

        # If the next character matches the current one, increase the count
        if x[i] == current_char:
            count += 1

        # If the next character does not match the current one perform 2 tasks
        else:
            # Add the current char and its count to the compressed output string
            compressed += current_char + str(count)
            # Change the current char to the newly found one, that doesnt match the previous
            current_char = x[i]
            # Start the count from 1 again
            count = 1
    
    # Add the final char and its count to the compressed output string (because the initial text ends)
    compressed += current_char + str(count)
    
    # Return compressed output string
    return compressed



# Initial Text
x = "aaavvvfdff"

# Calling function, providing params
compressed = compress_text(x)

# Returning compressed string value
print(compressed)  # Output: a3v3f1d1f2

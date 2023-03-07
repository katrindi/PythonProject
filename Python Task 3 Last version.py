# ----------Task 3----------

# Ask the user to enter a sequence of characters (x)
x = input("Please enter a sequence of characters (x) :")
# Print the length of characters (x)
x_len = len(x)
print("The length of the characters is : ", x_len)
# Ask the user to enter a single positive digit (y)
y = int(input("Please enter a single positive digit (y) : "))

# try,except for checking if "y" is a valid single-digit positive integer
try:
    y = int(y)
    # Check if the digit is positive
    if not (0 < y):
        raise ValueError("ERROR: y must be a single-digit positive integer")
except ValueError:
    print("ERROR: y must be a single-digit positive integer")
    exit()

# Check if "x" is not empty and has a length divisible by the length of "y"
if len(x) == 0:
    print("ERROR: You need to add characters. X cannot be empty")
    exit()
if len(x) % y != 0:
    print("ERROR: The length of x must be divisible by the length of y")
    exit()
# Default variables of split_number and start_point
split_number = y
start_point = 0
for n in range(y):
    # Splitting the sequence by indication of start point and the end point
    sub_word = x[start_point:(start_point + split_number)]
    # Increase the start point by the split number
    start_point += split_number
    unique_char = ""
    # Check if there is duplication in sub_word
    for char in sub_word:
        if char not in unique_char:
            unique_char += char
    print(unique_char)

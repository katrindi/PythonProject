#----------Task 3----------

# Ask the user to enter a sequence of characters (x)
# Ask the user to enter a single positive digit (y)
x = input("Hello. Here, you need to enter a sequence of characters(x): ")
y_spd = input("Please enter a SINGLE POSITIVE DIGIT(y): ")

# Check if "y" is a valid single-digit positive integer
try:
    y = int(y_spd)
    if not (0 < y < 10):
        raise ValueError("y must be a single-digit positive integer")
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

# Divide the text ("x") into equal parts, print only a unique characters (keep the characters in order)
for i in range(0, len(x), y):
    equal_parts = x[i:i+y]
    unique_chars = ""

    # Iterate through each character in the equal_parts and add it to unique_chars if it's not already there
    for char in equal_parts:
        if char not in unique_chars:
            unique_chars += char

    # Print the unique characters, keeping them in order
    print(unique_chars)


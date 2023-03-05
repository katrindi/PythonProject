# Task 1
# Create default variables which are strings.
n = ""
a = "ktur"
b = "ila"
# Check if the variable are strings,
try:
    # New function which will calculate the score
    def text_score(x, y, z):
        if len(x) == 0:
            print("X value cannot be an empty string")
        else:
            # Define the initializing score as 0
            score = 0
            # Check characters in y string
            for char_y in y:
                # If there is matching between the characters in positive number
                if char_y in x:
                    # Increase score by +1
                    score += 1
            for char_z in z:
                # If there is matching between the characters in negative number
                if char_z in x:
                    # Decrease score by -1
                    score -= 1
            # Print the final score, after comparison
            print(score)
    # Calling function with n,a,b values
    text_score(n, a, b)
# If the variables are not of string type - get error.
except:
    print("The variables should be a string!")
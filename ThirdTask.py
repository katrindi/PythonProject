# Task 3
x = input("Please enter a sequence of characters :")
# Calculate the length of the sequence
x_len = len(x)
print("The length of the sequence is : ", x_len)
try:
    y = int(input("Please enter a single digit : "))
    # Check if all requirements met
    if (y > 0) and (x_len % y) == 0:
        print("The condition are met, let's move to the next step")
        # Calculate the split numbers
        split_number = int(y)
        start_point = 0
        for n in range(y):
            # Splitting the sequence by indication of start point and the end point
            sub_word = x[start_point:(start_point+split_number)]
            # Increase the start point by the split number
            start_point += split_number
            unique_char = ""
            # Check if there is duplication in sub_word
            for char in sub_word:
                if char not in unique_char:
                    unique_char += char
            print(unique_char)
    else:
        print("Sorry but you conditions aren't met.")
except:
    print("You should provide a digit!")
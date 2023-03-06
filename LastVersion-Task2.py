# Task 2
data_list = [
    [1, 10, 34, 110, 400, 30, 20],
    [-5, -10, 55, 120, 30],
    [2, 67, 23, 78, 200],
]


# Function to filter the list
def filter_list(whole_list):
    # If data_list value is a list type
    if isinstance(whole_list, list):
        # Check each list in the data_list
        for sub_lists in data_list:
            # Check if the numbers in the list are between 10-100 range
            numbers_in_range = filter(lambda numbers: (numbers <= 100) and (numbers >= 10), sub_lists)
            # Save the numbers which are in range as filtered_list
            filtered_list = list(numbers_in_range)
            
            # Function to print the parameters
            def print_filter_list(a):
                # Check if the list isn't empty
                if a:
                    # Print the necessary values
                    print("Mean:", (sum(a) / len(a)), " |Max:", max(a), "|Min:",min(a), "|Sum:", sum(a))
                else:
                    print("There are not lists. ")
            print_filter_list(filtered_list)
    else:
        # Raise an error is the data_list is not a list
        raise TypeError("The data_list parameter should be a list!")


filter_list(data_list)

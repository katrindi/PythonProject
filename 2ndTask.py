# -- TASK 2 -- #

data_list = [
    [-1, 45, 23, 32, 999],
    [67, 99, 23],
    [23],
]


# Function to filter the list
def filter_list(whole_list):
    # If data_list value is a list type
    if isinstance(whole_list, list):
        # Check each list in the data_list
        for sub_list in whole_list:
            # Check if the numbers in the list are between 10-100 range
            numbers_in_range = filter(lambda number: 10 <= number <= 100, sub_list)
            # Save the numbers which are in range as filtered_list
            filtered_list = list(numbers_in_range)
            # Check if the list isn't empty
            if filtered_list:
                # Define mean,max,min and sum parameters
                mean_list = sum(filtered_list) / len(filtered_list)
                max_list = max(filtered_list)
                min_list = min(filtered_list)
                sum_list = sum(filtered_list)

                # Function to print the parameters
                def print_filtered_list(x, y, z, w):
                    # Print the necessary values
                    print("Mean: ", x, "| Min: ", z, " | Max: ", y, " | Sum:", w, "|")

                # Call the function which print the necessary values
                print_filtered_list(mean_list, max_list, min_list, sum_list)
            else:
                print("There are no numbers between 10 and 100 in the list.")
    else:
        # Raise an error if the data_list is not a list
        raise TypeError("The data_list parameter should be a list!")


# Call the filter function
filter_list(data_list)
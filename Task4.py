def subtractor(x):
    """
    Decorator that subtracts x from each return value of the decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # Subtract x from each value in the result tuple
            result = tuple(val - x for val in result)
            return result
        return wrapper
    return decorator


@subtractor(x=10)
def filter_list(a):
    """
    Filter a list to include only values between 10 and 100.
    Return the mean, maximum, minimum, and sum of the filtered list.
    """
    # Ensure input is a list
    if not isinstance(a, list):
        raise TypeError("Input must be a list")
    
    # Filter list to include only values between 10 and 100
    filtered_list = [num for num in a if num >= 10 and num <= 100]
    
    # Ensure filtered list is not empty
    if not filtered_list:
        raise ValueError("No values in input list between 10 and 100")
    
    # Calculate mean, maximum, minimum, and sum of filtered list
    mean = sum(filtered_list) / len(filtered_list)
    max_val = max(filtered_list)
    min_val = min(filtered_list)
    sum_val = sum(filtered_list)
    
    return mean, max_val, min_val, sum_val


def process_nested_list(b):
    """
    Call the filter_list function for each list in a nested list.
    Print the resulting mean, maximum, minimum, and sum for each list.
    """
    # Ensure input is a list of lists
    if not isinstance(b, list) or not all(isinstance(x, list) for x in b):
        raise TypeError("Input must be a list of lists")
    
    # Call filter_list for each list in the nested list and print results
    for nested_list in b:
        try:
            result = filter_list(nested_list)
            print(result)
        except (TypeError, ValueError) as e:
            print(f"Error processing {nested_list}: {e}")


# Example usage
data_list = [
    [-1, 45, 23, 32, 999],
    [67, 99, 23],
    [23],
]

process_nested_list(data_list)

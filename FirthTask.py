data_list = [
    [-1, 45, 23, 32, 999],
    [67, 99, 23],
    [23],
]
x = 10


def subtract_value(func):
    def wrapper(whole_list):
        for sub_lists in whole_list:
            numbers_in_range = filter(lambda numbers: (numbers < 100) and (numbers > 0), sub_lists)
            filtered_list = list(numbers_in_range)
            if filtered_list:
                modified_list = [number - 10 for number in filtered_list]
                print("Mean:", (sum(modified_list) / len(modified_list)), " |Max:", max(modified_list), "|Min:",
                      min(modified_list), "|Sum:", sum(modified_list))

    return wrapper


@subtract_value
def filter_return(whole_list):
    pass


filter_return(data_list)
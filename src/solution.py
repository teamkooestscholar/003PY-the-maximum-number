def find_maximum_and_minimum(numbers):
    if len(numbers) == 0:
        return None, None  # Return None for both max and min for an empty list

    max_number = numbers[0]
    min_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number
        elif number < min_number:
            min_number = number

    return max_number, min_number

# Example usage:
list_of_numbers = [1, 2, 3, 4, 5, 6]
max_value, min_value = find_maximum_and_minimum(list_of_numbers)
if max_value is not None and min_value is not None:
    print(f"MAXIMUM VALUE: {max_value}")
    print(f"MINIMUM VALUE: {min_value}")
else:
    print("The list is empty.")

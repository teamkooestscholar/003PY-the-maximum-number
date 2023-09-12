def find_max_min(numbers):
    if len(numbers) == 0:
        return None, None

    max_number = max(numbers)
    min_number = min(numbers)

    return max_number, min_number

input_numbers = input("Enter a list of integers separated by spaces: ")
try:
    numbers = [int(num) for num in input_numbers.split()]
    max_num, min_num = find_max_min(numbers)

    if max_num is not None and min_num is not None:
        print(f"Maximum number: {max_num}")
        print(f"Minimum number: {min_num}")
    else:
        print("The list is empty.")
except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")
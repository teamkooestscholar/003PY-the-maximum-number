def find_maximum_and_minimum(numbers):
    if len(numbers) == 0:
        return None, None

    max_number = max(numbers)
    min_number = min(numbers)

    return max_number, min_number

def find_maximum_and_minimum_from_user_input():
    user_input = input("Enter a list of integers separated by spaces: ")
    input_numbers = user_input.split()
    numbers = []

    for num in input_numbers:
        try:
            numbers.append(int(num))
        except ValueError:
            print("Invalid input! Please enter only integers separated by spaces.")
            return None, None

    maximum, minimum = find_maximum_and_minimum(numbers)

    if maximum is not None and minimum is not None:
        print("The maximum number is:", maximum)
        print("The minimum number is:", minimum)

find_maximum_and_minimum_from_user_input()

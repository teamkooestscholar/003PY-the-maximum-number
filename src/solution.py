# Write a function that returns the largest element in a list.
def find_maximum(numbers):
    if len(numbers) == 0:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def find_maximum_from_user_input():
    user_input = input("Enter a list of integers separated by spaces: ")
    input_numbers = user_input.split()
    numbers = []

    for num in input_numbers:
        try:
            numbers.append(int(num))
        except ValueError:
            print("Invalid input! Please enter only integers separated by spaces.")
            return None

    maximum = find_maximum(numbers)

    if maximum is not None:
        print("The maximum number is:", maximum)

find_maximum_from_user_input()


# Write a function that returns the largest element in a list.
def find_maximum_minimum(numbers):
    if len(numbers) == 0:
        return None, None

    max_number = min_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number
        elif number < min_number:
            min_number = number

    return max_number, min_number

numbers = []
for i in range(5):
    while True:
        try:
            number = int(input(f"Enter Your Number {i+1}: "))
            numbers.append(number)
            break
        except ValueError:
            print("Invalid input, enter an integer number.")

max_num, min_num = find_maximum_minimum(numbers)
if max_num is not None and min_num is not None:
    print(f"The Maximum number is: {max_num}")
    print(f"The Minimum number is: {min_num}")
else:
    print("Oops! The list is empty.")


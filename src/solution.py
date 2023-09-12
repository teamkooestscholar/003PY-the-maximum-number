def find_max(numbers):
    if not numbers:
        return None  # Return None for an empty list

    max_num = numbers[0]  # Assume the first number is the maximum

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num

while True:
    user_input = input("Enter a list of numbers separated by spaces (or type 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        break  # Exit the loop if the user types 'quit'

    user_numbers = [int(x) for x in user_input.split()]
    max_number = find_max(user_numbers)

    if max_number is not None:
        print("The maximum number is:", max_number)
    else:
        print("The list is empty.")
def find_maximum_and_minimum(numbers):
    if len(numbers) == 0:
        return None, None

    max_num = max(numbers)
    min_num = min(numbers)

    return max_num, min_num

def find_maxmin_from_user_input():
    user = input("Enter a list of integers separated by spaces: ")
    input_numbers = user.split()
    numbers = []

    for num in input_numbers:
        try:
            numbers.append(int(num))
        except ValueError:
            print("Invalid input! Please enter only integers separated by spaces.")
            return None, None

    maxi, mini = find_maximum_and_minimum(numbers)

    if maxi is not None and mini is not None:
        print("The maximum number is:", maxi)
        print("The minimum number is:", mini)

find_maxmin_from_user_input()
def find_max_and_min(numbers):
    if not numbers:
        return "The list is empty."
    
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num, min_num

# Input a list of integers from the user
user_input = input("Enter a list of integers separated by spaces: ")
user_input = user_input.split()
numbers_list = [int(num) for num in user_input]

# Call the function to find maximum and minimum
result = find_max_and_min(numbers_list)
if isinstance(result, tuple):
    maximum, minimum = result
    print(f"The maximum number is: {maximum}")
    print(f"The minimum number is: {minimum}")
else:
    print(result)

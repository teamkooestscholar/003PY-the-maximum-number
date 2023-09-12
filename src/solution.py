# Define a function to find the maximum and minimum numbers in a list of integers.
def find_max_and_min(numbers):
    if not numbers:  # Check if the list is empty
        return "The list is empty."

    max_num = max(numbers)  # Find the maximum number in the list
    min_num = min(numbers)  # Find the minimum number in the list
    return max_num, min_num  # Return the maximum and minimum as a tuple

# Input a list of integers from the user
user_input = input("Please enter a list of integers separated by spaces: ")
user_input = user_input.split()  # Split the input string into a list
numbers_list = [int(num) for num in user_input]  # Convert the list of strings to a list of integers

# Call the function to find the maximum and minimum
result = find_max_and_min(numbers_list)

# Check if the result is a tuple and display the maximum and minimum
if isinstance(result, tuple):
    maximum, minimum = result
    print(f"The maximum number is: {maximum}")
    print(f"The minimum number is: {minimum}")
else:
    print(result)  # Display an error message if the input list is empty
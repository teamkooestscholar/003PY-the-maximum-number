def find_maximum(numbers):
    if not numbers:
        return "List is empty."
    
    maximum = numbers[0]  # Initialize maximum with the first element
    
    for number in numbers:
        if number > maximum:
            maximum = number
    
    return maximum

# Input a list of numbers from the user
try:
    num_list = input("Enter a list of numbers separated by spaces: ").split()
    num_list = [float(num) for num in num_list]  # Convert input to a list of floats
except ValueError:
    print("Invalid input. Please enter a list of numbers separated by spaces.")
else:
    maximum = find_maximum(num_list)
    print(f"The maximum number in the list is: {maximum}")

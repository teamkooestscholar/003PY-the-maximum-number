def find_maximum(numbers):
    if not numbers:
        return None  # Handle empty list case
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def main():
    # Input a list of numbers from the user
    try:
        input_string = input("Enter a list of numbers separated by spaces: ")
        numbers = [int(x) for x in input_string.split()]
        
        # Call the find_maximum function to find the maximum number
        max_number = find_maximum(numbers)
        
        if max_number is not None:
            print("The maximum number is:", max_number)
        else:
            print("The list is empty. Cannot find a maximum.")
    
    except ValueError:
        print("Invalid input. Please enter a list of valid numbers separated by spaces.")

if _name_ == "_main_":
    main()

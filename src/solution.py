def find_maximum(numbers):
    if len(numbers) == 0:
        return None  # Bonus Challenge 1: Handle an empty list gracefully
    max_number = numbers[0]
    min_number = numbers[0]  # For Bonus Challenge 2
    for number in numbers:
        if number > max_number:
            max_number = number
        if number < min_number:  # For Bonus Challenge 2
            min_number = number
    return max_number, min_number  # For Bonus Challenge 2

if __name__ == "__main__":
    try:
        numbers = input("Enter a list of integers separated by spaces: ").split()
        numbers = [int(num) for num in numbers]

        if len(numbers) == 0:
            print("The list is empty.")  
            # Bonus Challenge 1: Print an appropriate message for an empty list
        else:
            result = find_maximum(numbers)
            max_num, min_num = result  
            # For Bonus Challenge 2
            print(f"The maximum number is: {max_num}")
            print(f"The minimum number is: {min_num}") 
            # For Bonus Challenge 2
    except ValueError:
        print("Invalid input. Please enter a list of integers.")
        
#Enter a list of integers separated by spaces: 54 56 78 100
#The maximum number is: 100
#The minimum number is: 54

#Enter a list of integers separated by spaces: 23, 4,4
#Invalid input. Please enter a list of integers.

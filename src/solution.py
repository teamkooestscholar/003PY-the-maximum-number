# Write a function that returns the largest element in a list.
def find_maximum(numbers):
    if len(numbers) == 0:
        return None, None  
    
    max_number = numbers[0]
    min_number = numbers[0]
    
    for number in numbers:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number
            
    return max_number, min_number

# input here:
numbers_list = [42, 70, 16, 69, -22, 50]
max_value, min_value = find_maximum(numbers_list)

if max_value is None:
    print("The list is empty.")
else:
    print(f"The maximum number is {max_value}.")
    
if min_value is None:
    print("The list is empty.")
else:
    print(f"The minimum number is {min_value}.")

# edit
# Write a function that returns the largest element in a list.
#Canane, Jewel Mae P.

def find_max_and_min(numbers):
    if not numbers:
        return "The list is empty."
    
    max_num = max(numbers)
    min_num = min(numbers)
    
    return max_num, min_num

number_list = [5, 2, 9, 1, 7, 3, 8]
result = find_max_and_min(number_list)

if isinstance(result, tuple):
    max_number, min_number = result
    print(f"Maximum number: {max_number}")
    print(f"Minimum number: {min_number}")
else:
    print(result)

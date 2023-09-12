def find_max_and_min(numbers):
    if not numbers:
        return "The list is empty"
    
    maximum = max(numbers)
    minimum = min(numbers)
    
    return maximum, minimum

numbers = [12, 45, 67, 23, 9]
result = find_max_and_min(numbers)
print(f"Maximum: {result[0]}, Minimum: {result[1]}")

empty_list_result = find_max_and_min([])
print(empty_list_result)
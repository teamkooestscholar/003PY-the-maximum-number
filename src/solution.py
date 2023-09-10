def find_maximum(numbers):
    if len(numbers) == 0:
        return "The list is empty. There is no maximum value."
    
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number

    return max_number

def find_maximum_and_minimum(numbers):
    if len(numbers) == 0:
        return "The list is empty. There are no maximum and minimum values."

    max_number = max(numbers)
    min_number = min(numbers)

    return max_number, min_number

numbers = [14, 25, 30, 0, 2, 26]
maximum = find_maximum(numbers)
maximum_and_minimum = find_maximum_and_minimum(numbers)

print(f"Numbers: {numbers}")
print(f"Maximum: {maximum}")
print(f"Maximum and Minimum: {maximum_and_minimum}")

empty_list = []
print(f"")
print(f"List = {empty_list}")
result = find_maximum_and_minimum(empty_list)
print(result)
    

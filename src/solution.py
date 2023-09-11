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

numbers1 = [3, 6, 2, 8, 1]
max1, min1 = find_maximum(numbers1)
print(f"Maximum: {max1}, Minimum: {min1}")

numbers2 = []
max2, min2 = find_maximum(numbers2)
print(f"Maximum: {max2}, Minimum: {min2}")

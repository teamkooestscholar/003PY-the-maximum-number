def find_maximum(numbers):
    if not numbers:  # Check if the list is empty
        return "The list is empty, there is no maximum or minimum value."

    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum


numbers = [5, 10, 15, 20, 25]
max_num, min_num = find_maximum(numbers)
print("The maximum number is:", max_num)
print("The minimum number is:", min_num)
def find_max_min(numbers):
    if len(numbers) == 0:
        return "The list is empty."
    else:
        max_num = max(numbers)
        min_num = min(numbers)
        return max_num, min_num

# Example usage:
my_list = [12, 5, 18, 3, 25, 9]
result = find_max_min(my_list)
print(f"Maximum number: {result[0]}, Minimum number: {result[1]}")

empty_list = []
result = find_max_min(empty_list)
print(result)  # This will print "The list is empty."
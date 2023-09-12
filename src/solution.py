# Write a function that returns the largest element in a list.
def find_max_min(numbers):
    
    maximum = max(numbers)
    minimum = min(numbers)
    
    return maximum, minimum


input_numbers = [12, 5, 8, 25, 3]
max_num, min_num = find_max_min(input_numbers)

print("Maximum:", max_num)
print("Minimum:", min_num)




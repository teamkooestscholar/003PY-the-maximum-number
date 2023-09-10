# # Write a function that returns the largest element in a list.
# def find_maximum(_):
#     pass


def find_max_and_min(numbers):
    if not numbers:
        return "Your list is empty, cannot find maximum or minimum."

    maximum = max(numbers)
    minimum = min(numbers)

    return maximum, minimum

# Example usage:
numbers_list = [5, 2, 9, 1, 7, 4, 8]
result = find_max_and_min(numbers_list)
print("Maximum:", result[0])
print("Minimum:", result[1])

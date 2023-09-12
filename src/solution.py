# Write a function that returns the largest element in a list.
def find_maximum_and_minimum(numbers):
  if len(numbers) == 0:
    return "The list is empty."
  max_number = numbers[0]
  min_number = numbers[0]
  for number in numbers:
    if number > max_number:
      max_number = number
    elif number < min_number:
      min_number = number
  return max_number, min_number

numbers = [56,6,7,13,24,12,51,34,134,5]
print(find_maximum_and_minimum(numbers))

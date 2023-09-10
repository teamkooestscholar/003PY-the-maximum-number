# Write a function that returns the largest element in a list.
def find_maximum(numbers):
    if len(numbers) == 0:
        return "The list is empty"
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    print("Maximum --> ",max_number)
    return max_number
    
    

n = [1,2,3,4,5]
find_maximum(n)
print("Minimum --> ", min(n))
      

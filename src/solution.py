def find_maximum(numbers):
    if not numbers:
       
        return None
    maximum = max(numbers)

    return maximum


number_list = [4, 7, 2, 9, 1, 11, 5]
maximum_number = find_maximum(number_list)
print("The maximum number is:", maximum_number)  

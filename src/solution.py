# function to return the largest and smallest number is list

def find_max_number(numbers):
    if len(numbers) == 0:
        print("list is empty")
    else:
        max_num = max(numbers)
        min_num = min(numbers)
        
        print(f"Max number: {max_num}, Min number: {min_num}")
    
list = [3, 4, 0, -1, 30, 44, 23, -5]

find_max_number(list)
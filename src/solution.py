# Write a function that returns the largest element in a list.
def find_max_number(numbers):
    """ return the maximum number in the list """
    if not numbers:
        return None  
    else:
        return max(numbers)

user_input = input("Please Enter a list of numbers: ")
input_values = user_input.split()  

int_list = []
for value in input_values:
    try:
        int_list.append(int(value))
    except ValueError:
        pass  

maximum = find_max_number(int_list)

if maximum is not None:
    print(f"The biggest value is: {maximum}")
else:
    print("Error: not valid")
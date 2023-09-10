def find_max(numbers):
    if not numbers:
        return None  
    else:
        return max(numbers)

user_input = input("Please Enter a list of numbers: ")
input_values = user_input.split()  

integer_list = []
for value in input_values:
    try:
        integer_list.append(int(value))
    except ValueError:
        pass  

maximum = find_max(integer_list)

if maximum is not None:
    print(f"The biggest number in this list is: {maximum}")
else:
    print("The list is not valid")

def find_max_min(nums_list):
    if len(nums_list) == 0:
        return "No numbers provided. Therefore nothing is made"  # When empty list occurs
    max_num = nums_list[0]
    min_num = nums_list[0]
    for num in nums_list:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num


def main():
    input_numbers = [] #The array in question 

    # Enter a list of numbers separated by spaces
    user_input = input("Enter a list of numbers separated by spaces: ")

    # Convert the user input into a list of integers
    try:
        input_numbers = [int(num) for num in user_input.split()]
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
        return

    result = find_max_min(input_numbers)

    if isinstance(result, str):  # Check if the result is a string
        print(result)  # Print the message
    else:
        max_number, min_number = result
        # Display the results
        print(f"Maximum number in the list: {max_number}")
        print(f"Minimum number in the list: {min_number}")


if __name__ == "__main__":
    main()
#added co author 
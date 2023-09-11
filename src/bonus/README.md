# Find the Maximum and Minimum Elements in a List

This Python program defines a function `find_maximum_and_minimum` that finds and returns both the maximum and minimum elements in a list of integers. It also includes a function `find_maximum_and_minimum_from_user_input` that allows the user to input a list of integers and then finds and displays both the maximum and minimum elements from that list.

## Function for Finding Maximum and Minimum Elements

The `find_maximum_and_minimum` function is designed to find both the maximum and minimum elements in a list of integers. It follows these steps:

```python
def find_maximum_and_minimum(numbers):
    """
    Find the maximum and minimum elements in a list of integers.

    :param numbers: A list of integers.
    :type numbers: list
    :return: A tuple containing the maximum and minimum elements in the list.
    :rtype: (int, int) or (None, None) if the list is empty.
    """
    if len(numbers) == 0:
        return None, None

    max_number = max(numbers)
    min_number = min(numbers)

    return max_number, min_number
```

- It checks if the input list `numbers` is empty, and if so, it returns `(None, None)` to indicate that there are no maximum and minimum elements.
- It uses the built-in `max()` and `min()` functions to find the maximum and minimum elements in the list, respectively.
- It returns a tuple containing both the maximum and minimum elements.

## Function for User Input and Output

The `find_maximum_and_minimum_from_user_input` function allows the user to input a list of integers separated by spaces and then finds and displays both the maximum and minimum elements from that list. It follows these steps:

```python
def find_maximum_and_minimum_from_user_input():
    user_input = input("Enter a list of integers separated by spaces: ")
    input_numbers = user_input.split()
    numbers = []

    for num in input_numbers:
        try:
            numbers.append(int(num))
        except ValueError:
            print("Invalid input! Please enter only integers separated by spaces.")
            return None, None

    maximum, minimum = find_maximum_and_minimum(numbers)

    if maximum is not None and minimum is not None:
        print("The maximum number is:", maximum)
        print("The minimum number is:", minimum)
```

- It prompts the user to enter a list of integers separated by spaces using `input()`.
- It splits the user input into individual numbers and stores them in the `input_numbers` list.
- It then attempts to convert each item in `input_numbers` into an integer and adds it to the `numbers` list. If the conversion fails (e.g., if the user enters non-integer values), it prints an error message and returns `(None, None)`.
- After collecting valid integers in the `numbers` list, it calls the `find_maximum_and_minimum` function to find both the maximum and minimum elements.
- Finally, it prints the maximum and minimum elements if they exist.

## Program Execution

The program concludes by calling `find_maximum_and_minimum_from_user_input()` to allow the user to input a list of integers and find both the maximum and minimum elements from that list.

You can run the program, enter a list of integers as prompted, and it will display both the maximum and minimum elements from your input.

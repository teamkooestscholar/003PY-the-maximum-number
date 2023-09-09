# EASY: 003 Python - Find the Maximum Number

## Description

Create a Python function that finds and returns the maximum number among a list of integers.

## Sample Solution

```python
def find_maximum(numbers):
    if len(numbers) == 0:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number
```

## Bonus Challenges

- Modify the function to handle an empty list gracefully and return an appropriate message or value. (Hint: you'll need a new conditional for this) **[+5 extra credit points]**

- Find and return both the maximum and minimum numbers in a single function call. (Hint: Python has a built in function called `min()` that does the opposite of `max()`) **[+5 extra credit points]**

## How to Answer?

- Navigate to the `src` directory and edit the `solution.py` file.

- Replace the `pass` with your solution.

#003 Write a function that returns the largest element in a list.
def Find_maximum(numbers):
    if len(numbers) == 0:
        return "The list is empty."
    else:
        max_num = max(numbers)
        min_num = min(numbers)
        print("The Minimum element is: ", min_num)
        print("The Maximum element is: ", max_num)
        return max_num, min_num

num = [100,20,10,3,80,6]
Find_maximum(num)

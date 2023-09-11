# Write a function that returns the largest element in a list.
def find_maximum(numbers):
    if len(numbers) == 0:
        return "The list is empty"
    else:
        maxnum = max(numbers)
        minnum = min(numbers)
        print("Minimum --> ", minnum)
        print("Maximum --> ", maxnum)
        return maxnum, minnum

    

n = [1,2,3,4,5]
find_maximum(n)

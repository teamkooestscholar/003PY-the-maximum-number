def find_maximum(numbers):
    if len(numbers) == 0:
        return "The list is empty"
    
    maxnum = numbers[0]
    minnum = numbers[0]

    for num in numbers:
        if num > maxnum:
            maxnum = num
        elif num < minnum:
            minnum = num

    print("Minimum -->", minnum)
    print("Maximum -->", maxnum)
    
    return maxnum, minnum

n = [1, 2, 3, 4, 5]
find_maximum(n)

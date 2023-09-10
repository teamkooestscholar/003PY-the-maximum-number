def max_and_min(nums):
    if not nums:
        return "List is empty. No max and min."

    max_num = max(nums)
    min_num = min(nums)

    return max_num, min_num

# Example usage:
nums1 = [5, 10, 2, 8, 15,19,59,69]
nums2 = []

result1 = max_and_min(nums1)
result2 = max_and_min(nums2)

if isinstance(result1, tuple):
    max1, min1 = result1
    print(f"Max in nums1: {max1}")
    print(f"Min in nums1: {min1}")
else:
    print(result1)

if isinstance(result2, tuple):
    max2, min2 = result2
    print(f"Max in nums2: {max2}")
    print(f"Min in nums2: {min2}")
else:
    print(result2)


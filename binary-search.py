#Perform Binary Search!

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_element = array[mid]
        if mid_element == target:
            return mid
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


array = [1, 2, 4, 5, 7, 9]
target = 5
result = binary_search(array, target)
print(result)
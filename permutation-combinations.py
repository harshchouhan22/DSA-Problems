from math import factorial

def getPermutation(n, k):
    nums = list(range(1, n+1))
    results = []

    k -= 1
    for i in range(n):
        index = k // factorial(n - 1 - i)
        results.append(str(nums.pop(index)))
        k %= factorial(n -1 -i)
    return "".join(results)



print(getPermutation(3, 3))
print(getPermutation(4, 9))  # Output: "2314"
print(getPermutation(3, 1)) 


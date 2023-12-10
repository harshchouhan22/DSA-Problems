import operator, time
import itertools

# Lists multiplication, addition, and division
List1 = [1, 2, 3, 4]
List2 = [8, 9, 10, 11]


def multiply_lists(list1, list2):
    start_time = time.time()
    # result = list(map(operator.mul, list1, list2))
    result = []
    for i in range(len(list1)):
        resultValues = list1[i] * list2[i]
        result.append(resultValues)
    end_time = time.time()
    duration = end_time-start_time
    print("Result: ", result, f"Time Take by the function is {duration:.6f}")
    return result


def subtractLists(l1, l2):
    result = list(map(operator.sub, l1, l2))
    return result

def addLists(l1, l2):
    results = list(map(operator.add, l1, l2))
    return results

# This function returns division of the given arguments.
def divideLists(l1, l2):
    results = list(map(operator.truediv, l1, l2))
    return results

#exponentiation 
def exponentials(l1, l2):
    results = list(map(operator.pow, l1, l2))
    return results

#mod, This function returns modulus of the given arguments. Operation – a % b.
def mudulusValue(l1, l2):
    results = list(map(operator.mod, l1, l2))
    return results

#This function checks – a < b.
def lessThan(l1, l2):
    results = list(map(operator.lt, l1, l2))
    return results

def greaterThen(l1, l2):
    results = list(map(operator.gt, l1, l2))
    return results

def checkEquals(l1, l2):
    results = list(map(operator.eq, l1, l2))
    return results

results = checkEquals(List1, List2)
print(results)



'''
DEMO TASK Codility

Write a function: def solution(A) that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:
* N is an integer within the range [1..100,000];
* each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def test1():
    input_list = [-1, 0, 2, 3, 4, 5, 6]
    val = solution(input_list)
    assert val == 1, f"Błąd: {val}"
    
def test2():
    input_list = [-5, -4, -3, -1, 0, 1, 2]
    val = solution(input_list)
    assert val == 3, f"Błąd: {val}"
    
def test3():
    input_list = [-1, 0, 2, 3, 4, 6]
    val = solution(input_list)
    assert val == 1, f"Błąd: {val}"
    
def test4():
    input_list = [-1,-22, -89, -76, -3, -1]
    val = solution(input_list)
    assert val == 1, f"Błąd: {val}"
    
def test5():
    input_list = [6,8,1,-3,4,0,-21]
    val = solution(input_list)
    assert val == 3, f"Błąd: {val}"
    
def test6():
    input_list = [-1,3,4,5,6]
    val = solution(input_list)
    assert val == 1, f"Błąd: {val}"
    
def test7():
    input_list = [0,1,2,3,4,5,6]
    val = solution(input_list)
    assert val == 7, f"Błąd: {val}"  

def solution(A):
    if not isinstance(A, list):
        raise TypeError("Expected data of list type")
        
    filtr = [x for x in A if x >= 0]
    
    # case 1: all numbers are negative
    if len(filtr) == 0:
        return 1
    
    # only zero left
    if len(filtr) == 1 and filtr[0] == 0:
        return 1
    
    # if 1 return 1 else if bigger return 1
    if len(filtr) == 1 and filtr[0] > 0:
        return 1
    
    data = sorted(list(set(filtr)))
    
    if 0 in data:
        data.remove(0)
            
    # case 2: smallest missing number will be always 1 if not in list
    minimum = min(data)
    if minimum != 1:
        return 1
    
    # if the biggest number is one, return 1
    maximum = max(data)
    if maximum == 1:
        return 1
    
    try:
        for i, _ in enumerate(data):
            if data[i+1]-data[i]>1:
                return data[i+1]-1
    except:
        return maximum+1

    

    

data  = [-1, 0, 1, 2, 3, 5]
print("Data: ", solution(data))

test1()
test2()
test3()
test4()
test5()
test6()
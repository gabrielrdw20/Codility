'''
TEST TASK Codility

Write a function: def solution(A) that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:
* N is an integer within the range [1..100,000];
* each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
import random 

def test1():
    outcome = solution([-1, 0, 2, 3, 4, 5, 6])
    assert outcome == 1, f"Error: {outcome}"
    
def test2():
    outcome = solution([-5, -4, -3, -1, 0, 1, 2])
    assert outcome == 3, f"Error: {outcome}"
    
def test3():
    outcome = solution([-1, 0, 2, 3, 4, 6])
    assert outcome == 1, f"Error: {outcome}"
    
def test4():
    outcome = solution([-1, -22, -89, -76, -3, -1])
    assert outcome == 1, f"Error: {outcome}"
    
def test5():
    outcome = solution([6, 8, 1, -3, 4, 0, -21])
    assert outcome == 2, f"Error: {outcome}"
    
def test6():
    outcome = solution([-1, 3, 4, 5, 6])
    assert outcome == 1, f"Error: {outcome}"
    
def test7():
    outcome = solution([0, 1, 2, 3, 4, 5, 6])
    assert outcome == 7, f"Error: {outcome}"  

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
        return filtr[0]
    
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
            # e.g. [1,3,4,5] check if 3-1 > 1
            if data[i+1]-data[i]>1:
                return data[i]+1
    except:
        return maximum+1

    
data  = [1,2,3,4,6,7,8,9,10,71]
print("Data: ", solution(data))

test1()
test2()
test3()
test4()
test5()
test6()

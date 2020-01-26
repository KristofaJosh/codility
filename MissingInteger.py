"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

def solution(A):
    Arr = list(set(A))
    print(Arr)

    for i, value in enumerate(Arr):
        print(Arr[0], i, value)
        if Arr[0] == 0:
            Arr.pop(0)
        if Arr[0] != 1:
            return 1
        if Arr[0] + i != value:
            ans = value - 1 if value > 0 else 1
            return ans
    return max(Arr) + 1

# print(solution([1,2,3,4,6]))


# print(solution([x for x in range(101)].extend([x for x in range(102, 200)])))


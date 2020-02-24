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
    A = set(A)
    B = {x for x in range(1, max(A) + 1)}

    # only positive numbers check
    if all(i < 0 for i in A):
        return 1

    # check if list are equal, return len + 1
    elif A == B:
        return len(A) + 1
    else:
        return min(list(B - A)) if list(B - A) else 1


print(solution([0]))

print(solution([1, 3, 6, 8, 4, 1, 2]))
#
# print(solution([1, 2, 3]))
#
# print(solution([-1, -2, -3]))

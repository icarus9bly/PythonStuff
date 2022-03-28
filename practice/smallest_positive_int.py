def solution(A):
    arr = [0] * 1000001
    for a in A:
        if a>0:
            arr[a] = 1
    for i in range(1, 1000000+1):
        if arr[i] == 0:
            return i

A1 = [1, 3, 6, 4, 1, 2]
A2 = [1, 2, 3]
A3 = [-1, -3]

solution(A1)
solution(A2)
solution(A3)
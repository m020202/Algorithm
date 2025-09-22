import sys, copy
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = list(map(str,input().rstrip()))

def calc(operator,a,b): # 단순 연산
    if operator=='+':
        return a+b
    elif operator=='-':
        return a-b
    else:
        return a*b

def calc_all(arr): # 전체 수식 계산
    idx = 0
    while len(arr) > 1:
        if arr[idx] == '+' or arr[idx] == '-' or arr[idx] == '*':
            arr = [str(calc(arr[idx],int(arr[idx-1]),int(arr[idx+1])))] + arr[idx+2:]
            idx = 0
        idx += 1
    return int(arr[0])

ans = -sys.maxsize
def func(idx,arr,state):
    global ans
    if idx >= len(arr):
        ans = max(ans,calc_all(arr))
    else:
        if state == 0:
            # 괄호 붙이기
            new_arr = arr[:idx-1] + [str(calc(arr[idx], int(arr[idx-1]), int(arr[idx+1])))] + arr[idx+2:]
            func(idx,new_arr,1)
        # 괄호 안 붙이기
        func(idx+2,arr,0)

func(1,arr,0)
print(ans)
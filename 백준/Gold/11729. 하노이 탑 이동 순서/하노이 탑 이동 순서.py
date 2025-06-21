import sys
input = sys.stdin.readline

n = int(input())

def hanoi(cur, start, end):
    if cur == 1:
        print(start, end)
    else:
        hanoi(cur-1, start, 6-start-end) # 1 -> 2로 옮기는 과정
        print(start, end) # 1 -> 3으로 옮기기 한 번에 가능하므로 바로 출력
        hanoi(cur-1, 6-start-end, end) # 2 -> 3로 옮기는 과정

print(2**n-1)
hanoi(n,1,3)

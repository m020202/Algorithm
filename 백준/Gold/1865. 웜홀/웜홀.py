from collections import deque
import sys
INF = sys.maxsize
input = sys.stdin.readline


def BF(arr):
    ch = [INF] * (N+1)
    for i in range(N):
        for s,e,t in arr:
            if ch[e] > ch[s] + t:
                ch[e] = ch[s] + t
                if i == N-1:
                    return True
    return False

T = int(input())
for _ in range(T):
    N,M,W = map(int,input().split())
    arr = []
    for _ in range(M):
        S,E,T = map(int,input().split())
        arr.append((S,E,T))
        arr.append((E,S,T))
    for _ in range(W):
        S,E,T = map(int,input().split())
        arr.append((S,E,-T))

    if BF(arr):
        print("YES")
    else:
        print("NO")

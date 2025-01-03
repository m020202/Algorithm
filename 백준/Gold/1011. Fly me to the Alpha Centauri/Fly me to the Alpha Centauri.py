n = int(input())

for _ in range(n):
    x,y = map(int,input().split())
    cur = y-x

    num = 1
    i = 1
    j = 1
    ans = 0
    while True:
        if ans > 0:
            print(ans)
            break
        for _ in range(2):
            num += i
            if num > cur:
                ans = j
                break
            j += 1
        i += 1






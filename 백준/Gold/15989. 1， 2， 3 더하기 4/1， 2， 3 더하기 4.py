def cal(n):
    ans = 0
    cur = n // 3
    for i in range(cur + 1):
        now = n - (i * 3)
        ans += (now // 2) + 1
    
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    print(cal(n))
n,k = map(int,input().split())
ch = [1] * (n+1)

for _ in range(k-1):
    cnt = 0
    for i in range(n+1):
        cnt += ch[i]
        ch[i] = cnt
    
print(ch[n] % 1000000000)
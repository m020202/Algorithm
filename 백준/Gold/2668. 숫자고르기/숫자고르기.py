n = int(input())
box1 = list(range(n+1))
box2 = [int(input()) for _ in range(n)]
box2.insert(0,0)
ans = []

def DFS(lst,i,num):
    global ans
    cur = box2[i]
    if ch[cur] == 1:
        return
    ch[cur] = 1
    lst.append(cur)
    if cur == num:
        ans += lst
        return
    return DFS(lst,cur,num)

for i in range(1,n+1):
    if i == box2[i]:
        ans.append(i)
    else:
        ch = [0] * (n+1)
        cur = box2[i]
        ch[cur] = 1
        DFS([cur],cur,i)

ans.sort()
ans = set(ans)
print(len(ans))
for i in ans:
    print(i)
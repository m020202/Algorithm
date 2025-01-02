n = int(input())
x = {}
box = []

for _ in range(n):
    i,j = map(int,input().split())
    box.append((i,j))
box.sort()
for i,j in box:
    x[i] = j

lt = 0  # 기준점보다 왼쪽 사람 수
rt = sum(x.values())  # 기준점보다 오른쪽 사람 수
lt_val = 0 # 왼쪽 총 거리
rt_val = 0 # 오른쪽 총 거리

# 위치가 0일 때
cur = box[0][1]
rt -= cur
for i in range(1,n):
    rt_val += (i * box[i][1])
ans = rt_val
idx = box[0][0]
for i in range(1, n):
    lt += cur
    lt_val += lt

    cur = box[i][1]
    rt_val -= rt
    rt -= cur
    if (lt_val + rt_val < ans):
        ans = lt_val + rt_val
        idx = box[i][0]
        
print(idx)




n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]
left = 0
for i in range(n):
    num = box[i][0] * box[(i+1)%n][1]
    left += num

right = 0
for i in range(n):
    num = box[i][0] * box[(i-1)%n][1]
    right += num

ans = (left - right) / 2
if ans < 0:
    ans = 0 - ans

print(round(ans,1))
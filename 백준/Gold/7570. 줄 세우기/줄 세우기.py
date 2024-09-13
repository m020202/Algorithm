# n = int(input())
# box = list(map(int,input().split()))

# tot = 1
# ans = 1
# for i in range(n-1):
#     if box[i] < box[i+1]:
#         tot += 1
#         ans = max(ans,tot)
#     else:
#         tot = 1


# print(n - ans)
n = int(input())
box = list(map(int,input().split()))
box.insert(0,0)

res = [0 for _ in range(n+1)]
for i in range(1,n+1):
    res[box[i]] = i

cnt = 1
max_len = -1

for i in range(1,n):
    if (res[i] < res[i+1]):
        cnt += 1

        if cnt > max_len:
            max_len = cnt
    else:
        cnt = 1

print(n-max_len if max_len != -1 else 0)
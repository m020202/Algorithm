import sys, copy
input = sys.stdin.readline
n = int(input())
box = [tuple(map(int,input().split())) for _ in range(n)]

# 정렬용
tmp = copy.deepcopy(box)
tmp.sort(key = lambda x : x[1])

# 각 튜플의 실제 위치
idx = {}
for i in range(n-1,-1,-1):
    idx[(tmp[i][0],tmp[i][1])] = i

k = set([tmp[i][0] for i in range(n)])

# 공 색깔에 속하는 크기들
dic = {}
for i in k:
    dic[i] = []

# 같은 색깔에 대한 본인 전까지 누적합
same = {}
for i in range(n):
    left = tmp[i][0]
    right = tmp[i][1]
    if len(dic[left]) == 0:
        same[(left,right)] = 0
    elif dic[left][-1] < right:
        same[(left, right)] = sum(dic[left])
    else:
        same[(left,right)] = same[(left,dic[left][-1])]
    dic[left].append(right)

# 총 누적합
ch = [0] * n
temp = [tmp[i][1] for i in range(n)]
for i in range(1,n):
    if tmp[i][1] == tmp[i-1][1]:
        ch[i] = ch[i-1]
    else:
        ch[i] = sum(temp[:i])

for i in range(n):
    c,s = box[i][0], box[i][1]
    cur = idx[(c,s)]
    print(ch[cur] - same[(c,s)])



import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    f = int(input())
    box = []
    dic = {}
    dic_cnt = {}
    idx = 0
    for _ in range(f):
        a,b = map(str,input().split())
        if a in dic and b in dic:
            if dic[a] == dic[b]:
                print(dic_cnt[dic[a]])
            else:
                dic_cnt[dic[a]] += dic_cnt[dic[b]]
                dic_cnt.pop(dic[b])
                rmv = dic[b]
                for i in dic:
                    if dic[i] == rmv:
                        dic[i] = dic[a]
                print(dic_cnt[dic[a]])
        elif a in dic:
            dic[b] = dic[a]
            dic_cnt[dic[a]] += 1
            print(dic_cnt[dic[a]])
        elif b in dic:
            dic[a] = dic[b]
            dic_cnt[dic[b]] += 1
            print(dic_cnt[dic[b]])
        else:
            idx += 1
            dic[a] = idx
            dic[b] = idx
            dic_cnt[idx] = 2
            print(2)


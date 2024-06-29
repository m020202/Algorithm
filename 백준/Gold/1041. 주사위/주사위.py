import sys
n = int(input())
box = list(map(int,input().split()))
dic = {}
dic[0] = 5
dic[5] = 0
dic[1] = 4
dic[4] = 1
dic[2] = 3
dic[3] = 2

if (n == 1):
    print(sum(box)-max(box))
    sys.exit()

def v2():
    ans = 100000
    for i in range(6):
        cur = box[i]
        rev = dic[i]
        for j in range(i+1,6):
            if j != rev:
                ans = min(ans,(cur+box[j]))
    return ans

def v3():
    ans = 10000
    ans = min(ans,box[0] + box[1] + box[3])
    ans = min(ans,box[0] + box[3] + box[4])
    ans = min(ans,box[0] + box[4] + box[2])
    ans = min(ans,box[0] + box[2] + box[1])

    ans = min(ans,box[1] + box[0] + box[2])
    ans = min(ans,box[1] + box[2] + box[5])
    ans = min(ans,box[1] + box[5] + box[3])
    ans = min(ans,box[1] + box[3] + box[0])

    ans = min(ans,box[2] + box[4] + box[5])
    ans = min(ans,box[2] + box[5] + box[1])
    ans = min(ans,box[2] + box[1] + box[0])
    ans = min(ans,box[2] + box[0] + box[4])

    ans = min(ans,box[3] + box[0] + box[1])
    ans = min(ans,box[3] + box[1] + box[5])
    ans = min(ans,box[3] + box[5] + box[4])
    ans = min(ans,box[3] + box[4] + box[0])

    ans = min(ans,box[4] + box[2] + box[5])
    ans = min(ans,box[4] + box[5] + box[3])
    ans = min(ans,box[4] + box[3] + box[0])
    ans = min(ans,box[4] + box[0] + box[2])

    ans = min(ans,box[5] + box[3] + box[4])
    ans = min(ans,box[5] + box[4] + box[2])
    ans = min(ans,box[5] + box[2] + box[1])
    ans = min(ans,box[5] + box[1] + box[3])

    return ans

m = min(box)
l = v2()
k = v3()


ans = (l * 4 + (n - 2) * m * 4) * (n - 1)
ans += k * 4 + (n - 2) * l * 4 + (n*n - 4*n + 4) * m

print(ans)
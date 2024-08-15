import sys
input = sys.stdin.readline
n,h = map(int,input().split())
top = []
bot = []
for i in range(n):
    if i%2==0:
        bot.append(int(input()))
    else:
        top.append(int(input()))

top.sort()
bot.sort()
ans = n
cnt = 0
def found(lt,rt,target,arr):
    while lt <= rt:
        mid = (lt + rt) // 2
        if arr[mid] < target:
            lt = mid + 1
        else:
            rt = mid - 1
    return lt

for i in range(1,h+1):
    min_bot = len(bot) - found(0,len(bot)-1,i-0.5,bot)
    min_top = len(top) - found(0,len(top)-1,h-i+0.5,top)
    tot = min_bot + min_top
    if ans == tot:
        cnt += 1
    elif tot < ans:
        cnt = 1
        ans = tot
print(ans,cnt)
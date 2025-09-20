import sys, copy
input = sys.stdin.readline
N,M,D = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# 적 위치
enemy_list = {}
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            enemy_list[(i,j)] = True

def killing(box,enemy):
    res = 0
    while enemy:
        die = set()
        # 각 궁수마다 죽일 적 탐색
        for i in box:
            tmp = False
            dist = D+1
            location = (0,M+1)
            for x,y in enemy:
                cur = abs(N-x) + abs(i-y)
                if cur <= D:
                    if cur < dist or (cur == dist and y < location[1]):
                        dist = cur
                        location = (x,y)
                        tmp = True
            if tmp:
                die.add(location)

        # 죽은 적이 있다면 리스트에서 제거
        for i in die:
            res += 1
            enemy.pop(i)

        # 적 이동
        new_enemy = {}
        for i,j in enemy:
            if i < N-1:
                new_enemy[(i+1,j)] = True
        enemy = new_enemy

    return res

ans = 0
def func(cnt,archer):
    global ans
    if cnt == 3:
        # 최댓값 구하기
        ans = max(ans,killing(archer, copy.deepcopy(enemy_list)))
    else:
        # 궁수 위치 선택
        last = archer[-1] if archer else -1
        for i in range(last+1,M):
            func(cnt+1, archer+[i])


func(0,[])
print(ans)
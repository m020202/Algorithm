import sys
input = sys.stdin.readline

def checking(numbers):
    numbers.sort()
    for i in range(n-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    box = [input()[:-1] for _ in range(n)]
    result = checking(box)
    if result:
        print("YES")
    else:
        print("NO")

import sys
input = sys.stdin.readline
sys.setrecursionlimit(65536)
tree = []
left = [-1] * (10001)
right = [-1] * (10001)
tree.append(int(input()))
idx = 1

def constructing(idx,cur):
    if tree[idx] > cur:
        if left[idx] == -1:
            tree.append(cur)
            left[idx] = len(tree)-1
            return len(tree)-1
        else:
            return constructing(left[idx], cur)
    else:
        if right[idx] == -1:
            tree.append(cur)
            right[idx] = len(tree) -1
            return len(tree)-1
        else:
            return constructing(right[idx],cur)

while True:
    try:
        cur = int(input())
        constructing(0,cur)               
    except:
        break
            
# 후위 순회
def postOrder(idx):
    if (left[idx] != -1):
        postOrder(left[idx])
    if (right[idx] != -1):
        postOrder(right[idx])
    print(tree[idx])

postOrder(0)
import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, k):
    queue.append(n)
    cnt = 0

    while queue:
        x = queue.popleft()
        dx = [x-1, x+1, x*2]
        for i in range(3):
            nx = dx[i]

            if nx == k:
                graph[nx] = graph[x] + 1
                return

            if 0 <= nx < 100001 and graph[nx] == 0:
                queue.append(nx)
                graph[nx] = graph[x] + 1


n, k = map(int, input().split())
graph = [0] * 100001
queue = deque([n])

if n == k:
    print(0)
else:
    bfs(n, k)
    print(graph[k])

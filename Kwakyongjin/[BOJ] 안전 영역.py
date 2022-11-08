import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, k):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = deque([])
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1 

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > k and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx, ny])


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

res = []
for k in range(0, 101):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and visited[i][j] == 0:
                cnt += 1
                bfs(i, j, k)
    res.append(cnt)
print(max(res))

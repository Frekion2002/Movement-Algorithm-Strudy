import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0 ,0], [0, 0, 1, -1]
tmp = 0
ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

def bfs(x, y):
    queue = deque([[x, y]])
    sea_count = []
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        sea = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
        
        if sea > 0:
            sea_count.append([x, y, sea])
    
    for x, y, sea in sea_count:
        graph[x][y] = max(0, graph[x][y] - sea)

    return 1


while ice:
    visited = [[0]*m for _ in range(n)]
    dellist = []
    cnt = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            cnt += bfs(i, j)
        
        if graph[i][j] == 0:
            dellist.append((i, j))
        
    if cnt > 1:
        print(tmp)
        break

    ice = set(ice) - set(dellist)
    ice = sorted(list(ice))

    tmp += 1
    
if cnt < 2:
    print(0)

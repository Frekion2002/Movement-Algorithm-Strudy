import sys
import math
input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    if n == 1:
        print(1)
        continue

    cnt = 0
    for i in range(n+1, 2*n+1):
        chk = True
        for j in range(2, int(math.sqrt(i)+1)):
            if i%j == 0:
                chk = False
                break
        
        if chk:
            cnt += 1
            continue
    
    print(cnt)

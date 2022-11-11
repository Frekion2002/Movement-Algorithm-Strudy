import sys
input = sys.stdin.readline

m, n = map(int, input().split())
cnt = 0

for num in range(m, n+1):
    tmp = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            tmp = False
            break
    
    if tmp and num != 1:
        print(num)

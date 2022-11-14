import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    chk = set()
    dic = {}
    
    while n != 1:
        for i in range(2, n+1):
            if n%i == 0:
                if i in chk:
                    dic[i] += 1
                    n //= i
                else:
                    chk.add(i)
                    dic[i] = 1
                    n //= i
                break

    lst = list(dic.items())
    for i in range(len(lst)):
        print(lst[i][0], lst[i][1])

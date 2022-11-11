import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = 1
n_fact = 1
k_fact = 1

for _ in range(k):
    n_fact *= n
    k_fact *= num
    num += 1
    n -= 1

print((n_fact//k_fact)%10007)

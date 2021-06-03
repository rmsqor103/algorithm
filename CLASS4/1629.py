import sys
input = sys.stdin.readline

def recur(a, b):
    if b == 1:
        return a % c
    else:
        tmp = recur(a, b//2)
        if b % 2==0:
            return tmp * tmp % c
        else:
            return tmp * tmp * a % c

a, b, c = map(int, input().split())

print(recur(a, b))


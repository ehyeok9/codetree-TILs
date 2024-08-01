from functools import cmp_to_key
from sys import stdin

input = stdin.readline

def compare(x, y):
    if x[0] == y[0]:
        if int(x+y) < int(y+x): return 1
        else: return -1
    elif int(x[0]) < int(y[0]): return 1
    else: return -1

if __name__=="__main__":
    n = int(input())
    nums = [
        input().strip()
        for _ in range(n)
    ]

    nums.sort(key=cmp_to_key(compare))

    print("".join(nums))
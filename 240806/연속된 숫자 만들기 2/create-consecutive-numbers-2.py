import sys
import math

input = sys.stdin.readline

def check(num):
    if num[0]+1 == num[1] and num[1]+1 == num[2]:
        return True
    return False

if __name__=="__main__":
    num = list(map(int, input().split()))
    
    if check(num):
        print(0)
    elif num[0]+ 2 == num[1] or num[1] + 2 == num[2]:
        print(1)
    else:
        print(2)
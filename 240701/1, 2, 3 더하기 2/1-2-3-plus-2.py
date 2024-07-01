import sys

input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    if n <= 2:
        print(1)
    else:
        memo = [0 for _ in range(n+1)]
        memo[1] = 1
        memo[2] = 1
        memo[3] = 3
        # 3 : 3 12 21 
        # 4 : 31 13 121
        # 5 : 23 32 212 131
        # 6 : 123 132 213 231 312 321
        
        # 1 1 3 3 4 6 9 12
        # 4 0
        
        
        # for i in range(3, n+1):
        #     memo[i] =
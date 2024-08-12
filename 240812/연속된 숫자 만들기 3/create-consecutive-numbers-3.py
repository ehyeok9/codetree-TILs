import sys

input = sys.stdin.readline

if __name__=="__main__":
    loc = list(map(int, input().split()))

    print(max(loc[1] - loc[0], loc[2] - loc[1]) - 1)
    

    # 1 5 6
    # 1 4 5
    # 1 3 4
    # 1 2 3
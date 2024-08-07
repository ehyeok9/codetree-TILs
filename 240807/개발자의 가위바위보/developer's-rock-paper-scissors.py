import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    cases = [
        [0, 0, 0, 0]
        for _ in range(4)
    ]

    for i in range(n):
        a,b = map(int, input().split())
        cases[a][b] += 1
    
    case1 = cases[1][3] + cases[2][1] + cases[3][2]
    case2 = cases[1][2] + cases[3][1] + cases[2][3]
    
    print(max(case1, case2))
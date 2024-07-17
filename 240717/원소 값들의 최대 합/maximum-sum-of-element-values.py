import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    sequence = list(map(int, input().split()))
    sequence.insert(0, 0)

    answer = 0
    for i in range(1,n+1):
        temp = 0
        loc = i
        for j in range(m):
            loc = sequence[loc]
            temp += loc
        answer = max(answer, temp)
    
    print(answer)
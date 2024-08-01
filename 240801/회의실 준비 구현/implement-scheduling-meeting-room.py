import sys

input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    meetings = [
        list(map(int, input().split()))
        for i in range(n)
    ]

    meetings.sort(key=lambda x : x[1])

    answer = 0
    prev = 0
    for i in range(n):
        if prev <= meetings[i][0]:
            answer += 1
            prev = meetings[i][1]

    print(answer)
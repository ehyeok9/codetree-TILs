import sys

input = sys.stdin.readline

def moving(sequence, loc):
    tmp = sequence[loc]
    sequence[loc] = sequence[tmp]
    sequence[tmp] = tmp
    return tmp


if __name__ == "__main__":
    n, m = map(int, input().split())
    sequence = list(map(int, input().split()))
    sequence.insert(0, 0)

    answer = 0
    for i in range(1,n):
        temp = 0
        for j in range(m):
            temp += moving(sequence, i)
        answer = max(answer, temp)

    print(answer)
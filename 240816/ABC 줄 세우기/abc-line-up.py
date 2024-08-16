import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    alphabets = input().split()

    answer = 0

    for i in range(n):
        for j in range(i+1, n):
            if alphabets[i] > alphabets[j]:
                alphabets[i], alphabets[j] = alphabets[j], alphabets[i]
                answer += 1

    print(answer)
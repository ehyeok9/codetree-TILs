import sys

input = sys.stdin.readline

def search(heights):
    global n, h, t

    answer = float("inf")

    for i in range(n-t):
        temp = 0
        for j in range(i, i+t):
            temp += abs(heights[j] - h)
        
        answer = min(answer, temp)

    return answer


if __name__ == "__main__":
    n, h, t = map(int, input().split())
    heights = list(map(int, input().split()))

    print(search(heights))
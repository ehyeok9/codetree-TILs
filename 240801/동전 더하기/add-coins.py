import sys

input = sys.stdin.readline

def greedy(coins):
    global n, k

    answer = 0
    
    for coin in reversed(coins):
        answer += k//coin
        k %= coin
    
    return answer

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = [
        int(input())
        for _ in range(n)
    ]

    print(greedy(coins))
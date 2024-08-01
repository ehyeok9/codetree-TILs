import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    answer = arr[0]
    cur = 0
    for i in range(len(arr)):
        if cur < 0:
            cur = arr[i]
        else:
            cur += arr[i]
        
        answer = max(answer, cur)
    
    print(answer)
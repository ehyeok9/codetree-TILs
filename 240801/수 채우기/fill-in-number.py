import sys

input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    
    answer = float("inf")
    for i in range(n//5 + 1):
        remainder = (n - 5 * i)
        if remainder % 2 == 0:
            answer = min(answer, i + remainder//2)
    
    if answer == float("inf"):
        answer = -1

    print(answer)
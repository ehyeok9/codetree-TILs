import sys

input = sys.stdin.readline

def isPalindrome(num):
    temp = list(str(num))
    if temp == temp[::-1]: return 1
    return 0

if __name__ == "__main__":
    x, y = map(int, input().split())
    
    answer = 0
    for num in range(x, y+1):
        answer += isPalindrome(num)

    print(answer)
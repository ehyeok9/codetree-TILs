import sys

input = sys.stdin.readline

def check(num):
    if num[0]+1 == num[1] and num[1]+1 == num[2]:
        return True
    return False

if __name__=="__main__":
    num = list(map(int, input().split()))
    
    answer = 0
    while True:
        # print(num)
        if check(num): break

        if num[1] - num[0] < num[2] - num[1]:
            num[2] = num[1] + 1
        else:
            num[0] = num[1] - 1
        
        answer += 1
        num.sort()
        
    
    print(answer)
import sys

input = sys.stdin.readline

if __name__=="__main__":
    A, B, x, y = map(int, input().split())
    
    answer = []
    # A -> B
    answer.append(abs(B-A))
    # A -> x -> y -> B
    answer.append(abs(x-A) + abs(B-y))
    # A -> y -> x -> B
    answer.append(abs(y-A) + abs(B-x))
    
    print(min(answer))
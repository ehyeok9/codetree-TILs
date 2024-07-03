import sys

input = sys.stdin.readline

def scan(n, rest, ldr, mbr):
    answer = 0
    for cust in rest:
        cust -= ldr
        answer += 1

        if cust > 0:
            answer += (cust // mbr)
            if cust % mbr != 0:
                answer += 1

    return answer
if __name__=="__main__":
    n = int(input())
    rest = list(map(int, input().split()))
    ldr, mbr = map(int, input().split())

    print(scan(n, rest, ldr, mbr))
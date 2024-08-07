import sys

input = sys.stdin.readline

def findMaximumSeat(seats):
    maxi = None
    for seat in seats:
        if seat == "": continue
        if maxi == None or len(maxi) < len(seat):
            maxi = seat
    return maxi

if __name__ == "__main__":
    n = int(input())
    seats =input().split('1')
    
    maxi = findMaximumSeat(seats)
    mid = len(maxi)//2
    
    temp = list(maxi)
    temp[mid] = "1"
    seats.remove(maxi)
    seats.extend("".join(temp).split('1'))
    
    answer = float("inf")
    for seat in seats:
        if seat == "": continue
        if len(seat) + 1 < answer:
            answer = len(seat) + 1

    print(answer)
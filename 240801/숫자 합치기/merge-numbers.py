import sys
import heapq

input = sys.stdin.readline

def greedy(nums):
    global n

    answer = 0
    
    heapq.heapify(nums)
    while(len(nums) != 1):
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        
        temp = a + b
        heapq.heappush(nums, temp)
        answer += temp
        # print(answer)
    
    return answer
        

if __name__=="__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    print(greedy(nums))
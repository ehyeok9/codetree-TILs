import sys

input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    nums = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    nums.sort(key = lambda x: x[1])

    pointer = n-1
    cur = 0
    answer = 0
    while cur <= pointer:
        # print(cur, pointer)
        tmp = nums[cur][1] + nums[pointer][1]
        answer = max(tmp, answer)
        
        minus = min(nums[cur][0], nums[pointer][0])
        # print(minus, nums[cur][0], nums[pointer][0])
        nums[cur][0] -= minus
        nums[pointer][0] -= minus

        if nums[cur][0] <= 0: cur += 1
        if nums[pointer][0] <= 0: pointer -= 1

    print(answer)
    # 가장 큰 값이랑 가장 작은 값을 더하자
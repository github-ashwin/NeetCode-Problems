import sys
def main():
    input = sys.stdin.readline
    n = int(input().strip())
    nums  = list(map(int,input().strip().split()))

    max_sum = nums[0]
    curr_sum = nums[0]

    # Kadane's Algorithm
    for i in range(1, n):
        curr_sum = max(nums[i], curr_sum + nums[i]) # discards the previous if the sum is less or continues to build the subarray
        max_sum = max(max_sum, curr_sum)

    print(max_sum)


if __name__== "__main__":
    main()
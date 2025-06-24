import sys
def main():

    input = sys.stdin.readline

    n = int(input().strip())

    nums = list(map(int,input().strip().split()))

    hmap = {}
    for i,val in enumerate(nums):
        hmap[val]=i

    round = 1
    for i in range(2,n+1):
        if hmap[i] < hmap[i-1]:
            round+=1

    print(round)

if __name__=="__main__":
    main()
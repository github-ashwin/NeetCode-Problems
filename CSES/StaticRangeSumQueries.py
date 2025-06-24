import sys

def main():
    input = sys.stdin.readline
    n,q = map(int,input().strip().split())

    nums = list(map(int,input().strip().split()))
    qr = []

    # for _ in range(q):

    #     start,stop = map(int,input().strip().split())
    #     qr.append([start,stop])

    # s=0

    # for i in range(q):
    #     s = sum(nums[((qr[i][0])-1):((qr[i][1]))])
    #     print(s)

    prefix = [0]*(n+1)

    for i in range(1,n+1):
        prefix[i] = prefix[i-1]+nums[i-1]
    
    for _ in range(q):
        start,stop = map(int,input().strip().split())
        qr.append([start,stop])

    for l,r in qr:
        print(prefix[r]-prefix[l-1])

        

if __name__=="__main__":
    main()
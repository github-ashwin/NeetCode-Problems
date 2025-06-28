import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    stick = list(map(int,input().strip().split()))

    stick.sort()

    median = stick[n//2]
    cost = 0

    for i in stick:
        cost +=abs(i-median)

    print(cost)



if __name__ == "__main__":
    main()
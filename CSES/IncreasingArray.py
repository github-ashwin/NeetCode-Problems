def main():
    n = int(input())
    num = list(map(int,input().split()))
    moves = 0

    for i in range(1,n):
        if num[i]<num[i-1]:
            moves += (num[i-1] - num[i])
            num[i] = num[i-1]
    
    print(moves)

if __name__ == "__main__":
    main()
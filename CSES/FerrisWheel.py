def main():
    n , x = map(int,input().split()) #no of children and max. weight
    p = list(map(int,input().split()))

    p.sort()

    count = 0

    i = 0
    j = n-1

    while i<=j:
        if p[i] + p[j] <=x:
            i +=1
        j-=1
        count+=1


    print(count)


if __name__ == "__main__":
    main()
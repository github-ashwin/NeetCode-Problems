def main():
    n,m,k = map(int,input().split()) # the number of applicants, the number of apartments, and the maximum allowed difference.
    a = list(map(int,input().split())) # appartment size
    b = list(map(int,input().split())) # size of appartments

    a.sort()
    b.sort()

    i = j = 0

    count=0

    while i<n and j<m:
        if abs(a[i] - b[j]) <= k:
            count+=1
            i+=1
            j+=1
        elif b[j] < a[i] - k:
            j+=1
        else:
            i+=1

    
    print(count)

if __name__ == "__main__":
    main()
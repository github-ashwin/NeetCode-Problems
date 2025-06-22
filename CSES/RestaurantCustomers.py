def main():
    n = int(input())
    arrival = []
    departure = []

    for _ in range(n):
        a,d = map(int,input().split())
        arrival.append(a)
        departure.append(d)
    
    arrival.sort()
    departure.sort()

    i = j = 0
    count = 0
    max_count = 0

    while i<n and j<n:
        if arrival[i]<departure[j]:
            count+=1
            max_count = max(max_count,count)
            i+=1
        else:
            count-=1
            j+=1

    print(max_count)

if __name__ == "__main__":
    main()
def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    t = list(map(int,input().split()))

    h.sort(reverse=True)

    avail = -1
    for customer in t:
        ticket_found = False
        for i in range(len(h)):
            if h[i] <= customer:
                print(h[i])
                h.pop(i)
                ticket_found = True
                break
        if not ticket_found:
            print(-1)

        

if __name__=="__main__":
    main()
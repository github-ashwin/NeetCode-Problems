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

"""
TO SOLVE TIMELIMIT EXCEEDED PROBLEM

from sortedcontainers import SortedList

def main():
    n, m = map(int, input().split())
    h = SortedList(map(int, input().split()))  # ticket prices
    t = list(map(int, input().split()))        # customer budgets

    for customer in t:
        idx = h.bisect_right(customer)
        if idx == 0:
            print(-1)
        else:
            print(h[idx - 1])
            h.pop(idx - 1)

if __name__ == "__main__":
    main()

"""
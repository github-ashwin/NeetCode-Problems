import sys # To solve Time Limit Exceeded Issue

def main():
    input = sys.stdin.readline # Faster Input
    n = int(input())
    movie = []

    for i in range(n):
        s,e = map(int,input().split())
        movie.append([e,s])

    count = 0
    current = 0
    movie.sort()

    for end,start in movie:
        if start >= current:
            count +=1
            current = end

    print(count)

if __name__ == "__main__":
    main()
import sys

def main():
    input = sys.stdin.readline

    n = int(input().strip())

    songs = list(map(int,input().strip().split()))

    seen = {}
    left = 0
    right = 0
    seq = 0

    for right,song in enumerate(songs):
        if song in seen and seen[song] >=left:
            left = seen[song]+1
        seen[song] = right
        seq = max(seq, right-left+1)

    print(seq)
    
if __name__ == "__main__":
    main()
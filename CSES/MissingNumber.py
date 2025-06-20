def main():
    n = int(input())
    arr = list(map(int, input().split()))
    total = n * (n + 1) // 2
    arr_sum = sum(arr)
    print(total - arr_sum)

if __name__ == "__main__":
    main()
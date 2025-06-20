def main():
    n = int(input())
    result = []
    result.append(str(n))

    if n >= 1 and n <= 10**6:
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = n * 3 + 1
            result.append(str(n))
        print(' '.join(result))

if __name__ == "__main__":
    main()
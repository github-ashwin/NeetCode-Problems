# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for _ in range(n):
    word = input().strip()
    chars = list(word)

    length = len(chars)
    i = length - 2

    # Find pivot from the right
    while i >= 0 and chars[i] >= chars[i + 1]:
        i -= 1

    if i == -1:
        print("no answer")
        continue  # Skip to next test case

    # Find smallest char to the right of pivot that's bigger than pivot
    j = length - 1
    while chars[j] <= chars[i]:
        j -= 1

    # Swap pivot and that char
    chars[i], chars[j] = chars[j], chars[i]

    # Reverse the part after pivot
    chars[i + 1:] = reversed(chars[i + 1:])

    print(''.join(chars))

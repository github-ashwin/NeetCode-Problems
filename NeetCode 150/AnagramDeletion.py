def remove_anagram_duplicates(words):
    seen = set()
    result = []

    for word in words:
        # Sorted signature
        signature = ''.join(sorted(word))
        if signature not in seen:
            seen.add(signature)
            result.append(word)
    return result


if __name__ == "__main__":
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    result = remove_anagram_duplicates(words)
    for w in result:
        print(w)

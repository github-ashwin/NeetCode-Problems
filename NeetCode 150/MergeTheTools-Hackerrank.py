def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        s = string[i:i+k]
        result = ''
        seen = set()
        for c in s:
            if c not in seen:
                seen.add(c)
                result +=c
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
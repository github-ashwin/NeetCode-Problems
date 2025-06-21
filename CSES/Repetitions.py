def main():
    seq = input().strip()
    max_count=1
    count=1

    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            count+=1
        else:
            count=1
        max_count = max(max_count,count)
    
    print(max_count)

if __name__== "__main__":
    main()
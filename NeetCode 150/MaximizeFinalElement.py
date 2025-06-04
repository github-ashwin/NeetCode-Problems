def maximizeFinalElement(arr, n):
    arr.sort()

    if (arr[0] != 1):
        arr[0] = 1
   
    for i in range(1, n):
        if (arr[i] - arr[i - 1] > 1):
            arr[i] = arr[i - 1] + 1

    return arr[n - 1]


if __name__ == '__main__':
    
    n = 4
    arr = [3, 1, 3, 4]
    
    max = maximizeFinalElement(arr, n)
    print(max)
def getMaximumMEX(arr):
    arr.sort()  
    mex = 0     
    for i in arr:
        if i>=mex:
            mex+=1
    return mex

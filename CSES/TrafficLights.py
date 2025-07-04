import sys
import bisect
from sortedcontainers import SortedList

input = sys.stdin.readline

x,n= map(int,input().strip().split()) # Length of street, Traffic Lights
pos = list(map(int,input().strip().split()))

lights = SortedList()
lights.add(0)
lights.add(x)

intervals = SortedList()
intervals.add(x)

for i in pos:
    idx = lights.bisect(i) # index where the light is inserted
    left = lights[idx-1] 
    right = lights[idx]

    intervals.discard(right-left)

    intervals.add(i - left)
    intervals.add(right - i)

    lights.add(i)

    print(intervals[-1], end=' ')
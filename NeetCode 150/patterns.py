"""
Pattern 1

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

"""

for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
print()
"""
Pattern 2

*
* *
* * *
* * * * 
* * * * *

"""

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
print()

"""
Pattern 3

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""

for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
print()

"""
Pattern 4

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""

for i in range(5):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
print()

"""
Pattern 5

* * * * *
* * * *
* * *
* *
*

"""

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
print()

"""
Pattern 6

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()


"""
Pattern 7

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

"""

for i in range(5):
    for x in range(0,(5-i-1)):
        print(" ",end=" ")
    for x in range(0,(2*i)+1):
        print("*",end=" ")
    print()

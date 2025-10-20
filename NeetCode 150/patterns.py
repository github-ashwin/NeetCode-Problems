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

# Intution:
# no of rows = 5
# star count = odd(1,3,5,7,9) (2*i-1)
# leading spaces = (4,3,2,1) (n-i)

n = 5
for i in range(1, n+1):
    space = n - i
    star = 2*i - 1
    print("  " * space + "* " * star)
print()
print()

"""
Pattern 8

* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *

"""

# Intution:
# no of rows = 5
# star count = odd(9,7,5,3,1) (2*(n-i)-1)
# leading spaces = (4,3,2,1) (i)

n = 5
for i in range(n):
    star = (2*(n-i)-1)
    space = i
    print("  "*space + "* "*star)
print()
print()

"""
Pattern 9

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *

"""

n = 5
for i in range(1, n+1):
    space = n - i
    star = 2*i - 1
    print("  " * space + "* " * star)

n = 5
for i in range(n):
    star = (2*(n-i)-1)
    space = i
    print("  "*space + "* "*star)
print()
print()


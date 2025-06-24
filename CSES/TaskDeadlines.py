import sys # To solve Time Limit Exceeded Issue
def main():

    input = sys.stdin.readline
    n = int(input().strip())
    task= []

    for _ in range(n):
        start,deadline = map(int,input().strip().split())
        task.append([start,deadline])

    task.sort()

    # print(task)

    current = 0
    reward = 0

    for i,j in task:
        current +=i
        reward +=(j-current)

    print(reward)

if __name__ == "__main__":
    main()
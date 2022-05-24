n = int(input())
arr = []
for _ in range(n):
    data = input().split()
    arr.append([data[0],data[1]])
arr.sort(key = lambda a: a[1])
for i in arr:
    print(i[0])
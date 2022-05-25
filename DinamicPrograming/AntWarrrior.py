n = int(input())
arr = list(map(int,input().split()))
d = [0] * (n+1) # 만약 n+1 로만 둔다면 TypeError: can only concatenate list (not "int") to list 에러가 뜬다.
d[0] = arr[0]
d[1] = arr[1]
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+arr[i])
print(d[n-1])


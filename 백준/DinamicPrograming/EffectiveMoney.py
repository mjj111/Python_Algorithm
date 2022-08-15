n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
d= [10001] * (m+1)

# d 인덱스 값만큼 최소한의 동전 갯수를 넣어줄 것이다.
# 해당 인덱스를 만약 i가 뺄 수 있다면 (a-i가 값이 존재한다면) d[j]는 d[j-arr[i]] 인덱스 값+1이다. 
# 이렇게 값을 수정 하다가 최소한의 갯수를 원하기 때문에 min을 통해 수정해준다.
d[0] = 0
for i in range(n):
    for j in range(arr[i],m+1):
        if d[j-arr[i]]!= 10001:
            d[j] = min(d[j],d[j-arr[i]]+1)

if d[m] == 10001:
    print(-1)
else: 
    print(d[m])
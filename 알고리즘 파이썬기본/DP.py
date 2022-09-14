n=int(input())
dt=[0]*30001
# 초기값 
for i in range(2,n+1):
    dt[i]=dt[i-1]+1    
    if i%2==0:
        dt[i]=min(dt[i],dt[i//2]+1)
    if i%3==0:
         dt[i]=min(dt[i],dt[i//3]+1)
    if i%5==0:
        dt[i]=min(dt[i],dt[i//5]+1)
        print(dt[n])

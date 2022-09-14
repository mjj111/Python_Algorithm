#임의의 배열
array=[4,5,0,1,9,7,6]

count=[0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1

# 정렬된 정보 확인
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')
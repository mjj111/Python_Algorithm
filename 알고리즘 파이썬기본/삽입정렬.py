#임의의 배열
array=[4,5,0,1,9,7,6]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j-1],array[j]=array[j],array[j-1]
        else:
            break
print(array)
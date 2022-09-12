#임의의 배열
array=[4,5,0,1,9,7,6]

for i in range(len(array)):
    min_idx=i
    for j in range(i+1,len(array)):
        if array[min_idx]>array[j]:
            min_idx=j
    array[i],array[min_idx]=array[min_idx],array[i]
print(array)
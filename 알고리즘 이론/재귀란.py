def BinarySearch(dataA,begin,end,target): 

    if begin>end:
        return -1
    else:
        mid = (begin + end ) // 2
        if dataA[mid] == target:
            return mid
        elif dataA[mid] > target:
            BinarySearch(dataA,begin,mid-1,target)
        else:
            BinarySearch(dataA,mid+1,end,target)
print(BinarySearch([1,2,3,4,5,6],0,6,4))



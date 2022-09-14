def binary_search(array,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if mid==array[mid]:
        global result
        result=mid
        return None
    if mid>array[mid]:
        binary_search(array,mid+1,end)
    else:
        binary_search(array,start,mid-1)
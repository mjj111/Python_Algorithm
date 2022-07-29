def solution(s):
    array=s.split(" ")
    int_array=[int(i) for i in array]

    return str(min(int_array))+" "+str(max(int_array))
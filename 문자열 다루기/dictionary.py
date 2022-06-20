# 1. 딕셔너리 생성
d = {'a': 123123}
# 2. 값 추가
d[999] = 10
# 숫자 키, 숫자 값
d['99'] = 111 
# 문자 키, 숫자 값
d['BlockDMask']="blog" 
# 문자 키, 문자 값
d['wow']=[1,2,3,4,5]
# 문자 키, 리스트 값
d[(1,2)]="this is value"
# 튜플 키, 문자 값
d[1]=(3,'a',5)
# 숫자 키, 튜플 값

if 'blog' in d.values(): # 딕셔너리 값들 중 
    print("hi")
if 'e' in d:   #딕셔너리 keys 값들중  d.keys()
    print("hi")
print(d.items())# d의 key와 value 값들을 둘다 뺴낸다. 이렇게 뺴낸 녀석을 sorted(d.items, key = lambda x : x[1]) 가능하다.
print("\n")

arr = {"a":[123,0], 'b':[122,3], 'c':[1234,2]}
print(arr['a'])
print(arr.items())

arr1 = sorted(arr.items(),key = lambda x :x[2])
print(arr1)
print(arr1[0])

 # 이렇게는 불가능하다. 
b= arr.items()
b.sort(key = lambda x : x[1])
print(b)
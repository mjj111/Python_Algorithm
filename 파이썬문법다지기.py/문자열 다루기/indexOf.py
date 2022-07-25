a= "hello evertbody"
jj = a.index("hello") # 지져스 이게 될 줄이야... 그냥 바로 찾을 수가 있다...
print(a)
print("hello 의 인덱스 :" + str(jj))
a.split()
print(a)
jj = a.index("l")
print("l의 인덱스 :",jj) # 우리는 , 와 + 로 프린트 할 수 있다.// , 할 경우 한칸 띄워진다. ㅋ 

jj = 'apple pineapple'.rindex('pl')
print('apple pineapple')
print("오른쪽 부터 찾은 pl:",jj,"\n")

print('apple pineapple')
print('pl 개수 :', jj)
jj = 'apple pineapple'.count('pl')
print('pl 개수 :', jj)
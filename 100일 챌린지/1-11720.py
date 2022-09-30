n = input()
# 리스트 자체로 m은 구성된다
# map을 통해 하나씩 받을 떄 마다 int로 받아드려진다.
# a = 12345  lista = list(a) 가 불가하다. 
m = list(map(int,input()))
result = 0
for i in m:
    result += i
print(result)


from itertools import permutations as P

pool = ['A', 'B', 'C']
print(list(map(''.join, P(pool, 2)))) 

nPr = P(pool, 2)
print(list(nPr))

h = 'ininije'
print(list(h)) # 굳이 for문으로 하나씩 접근할 필요없다..ㅋㅋ char배열로 만들어준다 
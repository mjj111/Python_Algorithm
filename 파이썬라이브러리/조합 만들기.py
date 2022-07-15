import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기

h = 'ininije'
print(list(h)) # 굳이 for문으로 하나씩 접근할 필요없다..ㅋㅋ char배열로 만들어준다 
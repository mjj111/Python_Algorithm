import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))
def dfs(y,x,num):
    if num==3:
        if check():
            print("YES")
            exit()
        else:
            return

    for i in range(y,n):
        for j in range(n):
            if i<=y and j<=x:
                continue
            if data[i][j]=='X':
                data[i][j]='O'
                dfs(i,j,num+1)
                data[i][j]='X'

for i in range(n):
    for j in range(n):
        if data[i][j] == 'X':
            data[i][j]='O'
            dfs(i, j, 1)
            data[i][j]='X'
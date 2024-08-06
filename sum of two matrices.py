a=[[1,2,3],[4,5,6],[3,4,5]]
b=[[3,2,1],[3,2,1],[3,2,1]]
res=[[0,0,0],[0,0,0],[0,0,0]]
row=3
col=3
for i in range(row):
    for j in range(col):
        res[i][j]=a[i][j]+b[i][j]
print(res)

x = [[5,7,9],
   [10,50,3],
   [3,7,8]]
y = [[5,7,10],
    [6,3,3],
    [3,1,5]]

z = [[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(3):
    for j in range(3):
        z[i][i] = x[i][j] + y[i][j]
for i in z:

    print(i)

n, m, k = map(int, input().split())
mat1 = []
for i in range(n):
    mat1.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        mat1[i][j] = mat1[i][j] * k

for i in range(n):
    for j in range(m):
        print(mat1[i][j], end = ' ')
    print()


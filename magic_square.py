
def magic_square(n):
    matrix = [[int(i) for i in input().split()] for i in range(n)]
    sum = 0
    for i in range(n):
        sum += matrix[0][i]
    total_row = 0
    total_col = 0
    main_diagonal = 0
    antidiagonal = 0
    for i in range(n):
        for j in range(n):
            total_row += matrix[i][j]
            total_col += matrix[j][i]
            if i == j:
                main_diagonal += matrix[i][j]
            if (i == n - j - 1) and (j == n - i - 1):
                antidiagonal += matrix[i][j]
        if total_row != sum or total_col != sum:
            return 'NO'
        else:
            total_row = 0
            total_col = 0
    if main_diagonal != sum or antidiagonal != sum:
        return 'NO'
    return 'YES'


n = int(input())
result = magic_square(n)
print(result)

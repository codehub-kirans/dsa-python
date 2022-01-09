def uniquePaths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return uniquePaths(rows, columns -1) + uniquePaths(rows - 1, columns)

#Test
print(uniquePaths(3,7))
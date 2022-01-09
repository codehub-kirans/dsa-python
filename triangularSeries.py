def triangularSeries(num):
    if num == 0:
        return 0
    return num + triangularSeries(num - 1)

#Test
print(triangularSeries(6))
a = [[1,2,3],[4,5,6],[7,8,9]]
print(a[0])
print(enumerate(a[0]))
for index, item in reversed(list(enumerate(a[1]))):
    print(index)
    print(item)
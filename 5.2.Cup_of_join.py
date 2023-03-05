def join(*lists,sep='-'):
    l=[]
    for i in range(len(lists)):
        for j in lists[i]:
            l.append(j)
        if (i + 1 != len(lists)):
            l.append(sep)
    if not(l):
        return None
    return l


print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())
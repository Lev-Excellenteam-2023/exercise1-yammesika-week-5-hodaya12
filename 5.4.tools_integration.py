def interleave(*iterables ):
    lenghts=list(map(len,iterables))
    max1=max(lenghts)
    for i in range(max1):
        for j in iterables:
            if i<len(j):
                yield j[i]





l=[]
for i in interleave('abcgt', [1, 2, 3], ('!', '@', '#',4)):
    l.append(i)
print(l)
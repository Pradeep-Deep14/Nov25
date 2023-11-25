def f1(a,b=[]):
    b.append(a)
    return b
print (f1(2,[3,4]))

#[3, 4, 2]
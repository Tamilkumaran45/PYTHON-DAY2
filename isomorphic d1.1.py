def isIso(x,y):
    if len(x)!=len(y):
        return False
    for i in range(len(x)):
        count=0
        if x.count(x[i])!=y.count(y[i]):
            return False
        return True
print(isIso("Egg","Add"))
print(isIso("Foo","Bar"))
print(isIso("Paper","Title"))
print(isIso("fry","sky"))
print(isIso("apples","apple"))

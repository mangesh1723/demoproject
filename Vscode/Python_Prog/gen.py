def fun():
    i=1
    while i<=100:
        yield i
        i+=1
print(fun())
x=fun()
print(next(x))
print(list(x))   


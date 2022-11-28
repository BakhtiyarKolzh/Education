seq=[1,2,3,4]

def times2(var):
    return  var*2

a=list(map(times2, seq))
print("Var1",a)

b=list(map(lambda var: var*2, seq))
print("Var2",b)

c=list(filter(lambda item: item%2==0, seq))
print("Var3",c)

d=list(filter(lambda item: item%2==1, seq))
print("Var3",d)
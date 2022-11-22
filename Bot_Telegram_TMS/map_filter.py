def times2(var):
    return var*2

seq =[1,2,3,4]

print(list(map(times2, seq)))

print(list(map(lambda var: var*2, seq)))

print(list(filter(lambda item: item%2==0, seq)))
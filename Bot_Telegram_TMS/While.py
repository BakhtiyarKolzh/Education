'''
def go_down(n: int) -> list[int]:
    s = list()
    while n >= 1:
        s.append(n)
        n = n//2
    return s

res = go_down(10)

for n in res:
    print(n)
'''

'''
def sum_num_square_less_than(n: int) -> int:
    i = 0
    summa=0
    while i**2 <= n:
        summa+=i
        i += 1

    return summa

print(sum_num_square_less_than(27))
'''
'''
def find_k(n: int) -> int:
    k=0
    while n!=(k**2)//3 % 50:
        k=k+1
    return k

'''













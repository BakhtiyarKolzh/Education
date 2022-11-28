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
Дана функция
super_hash(k) = (k**2)//3 % 50
которая вычисляет хэш значение для любого целого числа. Значение всегда между 0 и 49.
Найдите такое наименьшее k, хэш которого даёт число n.

Например, если дано число n=33, нужно найти k=10, потому что super_hash(10) == 33

Не пытайтесь понять, как работает хэш функция, это не важно, 
просто перебирайте все значения, пока не найдёте такое k, что super_hash(k) == n.

НЕ ИСПОЛЬЗОВАТЬ FOR!'''

def find_k(n: int) -> int:
    while (n ** 2) // 3 % 50:
        return (n ** 2) // 3 % 50
print(find_k(0))















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


def sum_num_square_less_than(n: int) -> int:
    i = 0
    while i**2 <= n:
        # обязательно измените значение i, иначе зависнет
        ...
    return ...

























'''
def merge(a: list[int], b: list[int]) -> list[int]:
    c: list[int] = list()
    for i in range(max(len(a), len(b))):
        if i<len(a):
            c.append(a[i])
        if i<len(b):
            c.append(b[i])
    return c


assert merge([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
'''
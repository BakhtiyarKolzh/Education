
# import  math
#
# def test(degree: float) -> float:
#     rad = math.radians(degree)
#     if rad >= 0 and  rad <= math.pi/2:
#         return math.degrees(rad)
#     else:
#         return -math.degrees(rad)
#
#
# degree = int(input())
#
# result = test(degree)
# print(result)

# 0,99619469809
# -0,99619469809
#
# 0,70710678118
# 0,70710678118
#
#
#
# sin(45)
# 0,70710678118
#
# sin(225)
# −0,70710678118
# def divisible_by_three(a: list) -> list:
#     b = []
#     for i in a:
#         if i%3==0:
#             b.append(i)
#     return b
#
# a=[1, 2, 3, 4, 5, 6]
#
# print(divisible_by_three(a))



# def doubles(s: str) -> int:
#     count=0
#     for i in range(len(s)-1):
#         a=s[i]
#         if a==s[i+1]:
#             count+=1
#     return count
#
# s="ccdd eeff"
# print(doubles(s))




# def more_spaces(s: str) -> str:
#     for i in s:
#         a=s.split()
#     return a
#
#
#
#
# s = "Hello, world! "
# print(more_spaces(s))
#

# s="This"
# def add_hello(s: str) -> str:
#     r=s.replace("This", "This hello" ,1)
#     print(r)
#     return r
#
#
# add_hello(s)

# s="hello"
# def second_is_a(s: str) -> str:
#     r=s[:1] + "A"+s[2:]
#     print(r)
#     return r
#
# second_is_a(s)
# s="abc"
# def count_letters(s: str) -> int:
#     count=0
#     for i in s:
#         count+=1
#
#     return count
#
# count_letters(s)

def findDog(x):
    if '' in x:
        return True
    else:
        return False



x='Is there a dog here?'
print(findDog(x))







































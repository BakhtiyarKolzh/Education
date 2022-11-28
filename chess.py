"""

x1 = 4
y1 = 4
x2 = 5
y2 = 4

def is_rook_move_ok(x1: int, y1: int, x2: int, y2: int) -> bool:
    if (x1+y1+x2+y2)%2!=0:
        return True
    else:
        return False

res=is_rook_move_ok(x1,y1,x2,y2)
print(res)

"""




"""
#Korol

def is_rook_move_ok(x1: int, y1: int, x2: int, y2: int) -> bool:
    if (-1 <= x1-x2 <= 1 and x1-x2!=0) and (-1 <= y1-y2 <= 1 and y1-y2!=0):
        return True
    if (-1 <= x1-x2 <= 1 and x1-x2==0) and (-1 <= y1-y2 <= 1 and y1-y2!=0):
        return True
    if (-1 <= x1-x2 <= 1 and x1-x2!=0) and (-1 <= y1-y2 <= 1 and y1-y2==0):
        return True
    else:
        return False


assert is_rook_move_ok(5,5,4,4) == True
assert is_rook_move_ok(5,5,5,6) == True
assert is_rook_move_ok(4,5,4,6) == True
assert is_rook_move_ok(5,4,6,4) == True
assert is_rook_move_ok(5,4,4,4) == True
assert is_rook_move_ok(5,4,4,5) == True
assert is_rook_move_ok(5,4,6,6) == False
assert is_rook_move_ok(5,4,5,4) == False
assert is_rook_move_ok(5,4,6,6) == False
"""

"""
#Slon

def is_bishop_move_ok(x1: int, y1: int, x2: int, y2: int) -> bool:
    if abs(x1 - x2) == abs(y1 - y2):
        return True
    else:
        return False

assert is_bishop_move_ok(5,5,7,7) == True
assert is_bishop_move_ok(5,5,3,7) == True
assert is_bishop_move_ok(5,5,3,3) == True
assert is_bishop_move_ok(5,5,7,3) == True
assert is_bishop_move_ok(5,5,8,8) == True
assert is_bishop_move_ok(5,5,8,7) == False
assert is_bishop_move_ok(5,5,7,8) == False
assert is_bishop_move_ok(5,5,3,2) == False
"""

"""
#Ferz
def is_queen_move_ok(x1: int, y1: int, x2: int, y2: int) -> bool:
    if (x1 and y1 and x2 and y2) <=8:
        if abs(x1-x2) <= 1 and abs(y1-y2) <= 1 or x1 == x2 or y1 == y2:
            return True
        if abs(x1 - x2) == abs(y1 - y2):
            return True
        else:
            return False
    else:
        return False


assert is_queen_move_ok(5,5,7,5) == True
assert is_queen_move_ok(5,5,7,7) == True
assert is_queen_move_ok(5,5,5,3) == True
assert is_queen_move_ok(5,5,3,5) == True
assert is_queen_move_ok(5,5,1,2) == False
assert is_queen_move_ok(5,5,2,8) == True
assert is_queen_move_ok(5,5,3,8) == False
assert is_queen_move_ok(5,5,4,8) == False
assert is_queen_move_ok(5,5,9,9) == False
"""



"""
#Horse
def is_knight_move_ok(x1: int, y1: int, x2: int, y2: int) -> bool:
    if (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 2 == y2 or y1 + 2 == y2):
        return True
    elif (x1 - 2 == x2 or x1 + 2 == x2) and (y1 - 1 == y2 or y1 + 1 == y2):
        return True
    else:
        return False


assert is_knight_move_ok(1,1,1,4) == False
assert is_knight_move_ok(1,1,8,8) == False
assert is_knight_move_ok(2,4,3,2) == True
assert is_knight_move_ok(6,2,8,3) == True
assert is_knight_move_ok(5,2,4,4) == True
assert is_knight_move_ok(2,8,3,7) == False
assert is_knight_move_ok(2,8,3,5) == False
"""








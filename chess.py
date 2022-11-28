
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

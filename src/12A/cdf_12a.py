passwd= [input(), input(), input()]
def is_symetric(p):
    if p[0][0] != p[2][2]:
        return False
    elif p[0][1] != p[2][1]:
        return False
    elif p[0][2] != p[2][0]:
        return False
    elif p[1][0] != p[1][2]:
        return False
    else:
        return True
if is_symetric(passwd):
    print("YES")
else:
    print("NO")

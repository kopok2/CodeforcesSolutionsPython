def is_increasing(a):
    for x in range(a.__len__()-1):
        if a[x] >= a[x+1]:
            return x

    return True


d = int(input().split(" ")[1])
b = [int(x) for x in input().split(" ")]
i = 0
#d = 1
#b = [1 for x in range(2000)]
while True:
    #print(b)
    z = is_increasing(b)
    if z is True:
        break
    else:
        for x in range(z+1, len(b)):
            if b[x] <= b[z]:
                b[x] += d
                i += 1
        
print(i)
    
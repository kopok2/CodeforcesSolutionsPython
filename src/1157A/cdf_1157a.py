def f(x):
    x = x + 1
    while not x % 10:
        x = x / 10
    return int(x)
x = int(input())
i =0
a = []
while True:
    y = x
    for z in range(i):
        y = f(y)
    if y in a:
        break
    a.append(y)
    i +=1
print(len(a))

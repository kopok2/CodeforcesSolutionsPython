i = input().split(" ")
n = int(i[0])
m = int(i[1])
flag = [input() for x in range(n)]
previous = ""
result = True
for row in flag:
    if not row == row[0]*m:
        result = False
    if row == previous:
        result = False
    previous = row
if result:
    print("YES")
else:
    print("NO")

inp = input().split(" ")
n = int(inp[0])
max_height = int(inp[1])
restrictions = int(inp[2])

restriction_map = [max_height for x in range(n)]
for x in range(restrictions):
    restr = [int(y) for y in input().split(" ")]
    for z in range(restr[0]-1, restr[1]):
        if restriction_map[z] > restr[2]:
            restriction_map[z] = restr[2]
profit = [x**2 for x in restriction_map]
print(sum(profit))
    
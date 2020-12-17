t = int(input())

for _ in range(t):
	n, m = [int(x) for x in input().split(" ")]
	perm = [int(x) for x in input().split(" ")]
	exp = []
	for _1 in range(m):
		exp.append([float(x) for x in input().split(" ")])
	x = -1
	for i in range(n, 0, -1):
		if perm[i-1] != i:
			x = i
			break
	if x == -1:
		print(1)
		continue
	valid_exp = [experiment for experiment in exp if experiment[0] >= x]
	prob_unsorted = 1
	for experiment in valid_exp:
		prob_unsorted *= (1 - experiment[1])
	print(1 - prob_unsorted)

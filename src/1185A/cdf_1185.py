nums = input().split(" ")
d = int(nums[3])
positions = [int(x) for x in (nums[0], nums[1], nums[2])]
positions.sort()
perf_time = 0
if positions[1] - positions[0] < d:
    perf_time += d - (positions[1] - positions[0])
if positions[2] - positions[1] < d:
    perf_time += d - (positions[2] - positions[1])
print(perf_time)
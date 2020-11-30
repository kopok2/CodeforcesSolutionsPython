import math


class CodeforcesTask158BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.groups = []

    def read_input(self):
        self.n = int(input())
        self.groups = [int(x) for x in input().split(" ")]

    def process_task(self):
        group_cnt = [0] * 4
        for g in self.groups:
            group_cnt[g - 1] += 1
        needed_4 = group_cnt[3]
        needed_3_1 = group_cnt[2]
        group_cnt[0] -= min(group_cnt[0], group_cnt[2])
        needed_2 = group_cnt[1] // 2 + group_cnt[1] % 2
        if group_cnt[1] % 2:
            group_cnt[0] -= min(group_cnt[0], 2)
        needed_1 = math.ceil(group_cnt[0] / 4)
        needed = needed_4 + needed_3_1 + needed_2 + needed_1
        self.result = str(needed)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask158BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

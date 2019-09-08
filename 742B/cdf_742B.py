class CodeforcesTask742BSolution:
    def __init__(self):
        self.result = ''
        self.n_x = []
        self.array = []

    def read_input(self):
        self.n_x = [int(x) for x in input().split(" ")]
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        nums = {}
        for a in self.array:
            if a in nums:
                nums[a] += 1
            else:
                nums[a] = 1
        pair_cnt = 0
        for a in self.array:
            b = a ^ self.n_x[1]
            if b != a:
                if b in nums:
                    pair_cnt += nums[b]
            else:
                if nums[b] > 1:
                    pair_cnt += nums[b] - 1

        self.result = str(pair_cnt // 2)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask742BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

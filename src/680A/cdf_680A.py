class CodeforcesTask680ASolution:
    def __init__(self):
        self.result = ''
        self.nums = []

    def read_input(self):
        self.nums = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.nums.sort()
        if len(set(self.nums)) == 2:
            if max([self.nums.count(x) for x in list(set(self.nums))]) == 3:
                self.result = str(min(self.nums[0] * self.nums.count(self.nums[0]), self.nums[-1] * self.nums.count(self.nums[-1])))
            else:
                self.result = str(self.nums[0] + self.nums[-1])
        elif len(set(self.nums)) == 5:
            self.result = str(sum(self.nums))
        elif len(set(self.nums)) == 1:
            self.result = str(self.nums[0] * 2)
        elif len(set(self.nums)) == 4:
            rep = [x[0] for x in [(y, self.nums.count(y)) for y in list(set(self.nums))]if x[1] == 2][0]
            self.result = str(sum(self.nums) - 2 * rep)
        else:
            if max([self.nums.count(x) for x in list(set(self.nums))]) == 3:
                d = 3
            else:
                d = 2
            rep = [x[0] for x in [(y, self.nums.count(y)) for y in list(set(self.nums))] if x[1] > 1]
            rep.sort()
            self.result = str(sum(self.nums) - d * rep[-1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask680ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

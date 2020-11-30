class CodeforcesTask318ASolution:
    def __init__(self):
        self.result = ''
        self.nums = []

    def read_input(self):
        self.nums = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.nums[0] % 2:
            if self.nums[1] <= (self.nums[0]+1)/2:
                self.result = str(int(self.nums[1]*2 - 1))
            else:
                self.result = str(int((self.nums[1] - (self.nums[0]+1)/2)*2))
        else:
            if self.nums[1] <= (self.nums[0])/2:
                self.result = str(int(self.nums[1]*2 - 1))
            else:
                self.result = str(int((self.nums[1] - (self.nums[0])/2)*2))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask318ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

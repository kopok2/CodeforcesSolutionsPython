class CodeforcesTask190ASolution:
    def __init__(self):
        self.result = ''
        self.passengers = []

    def read_input(self):
        self.passengers = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.passengers[0]:
            if self.passengers[0] >= self.passengers[1]:
                min_fares = self.passengers[0]
            else:
                min_fares = self.passengers[1]
            if self.passengers[1]:
                max_fares = self.passengers[0] + self.passengers[1] - 1
            else:
                max_fares = self.passengers[0]
            self.result = "{0} {1}".format(min_fares, max_fares)
        else:
            if self.passengers[1]:
                self.result = "Impossible"
            else:
                self.result = "0 0"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask190ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

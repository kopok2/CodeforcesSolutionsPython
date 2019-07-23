def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count


class CodeforcesTask23ASolution:
    def __init__(self):
        self.result = ''
        self.string = ''

    def read_input(self):
        self.string = input()

    def process_task(self):
        o_max = 0
        for x in range(len(self.string)):
            for y in range(x):
                m = occurrences(self.string, self.string[y:x])
                if m >= 2:
                    o_max = max(x - y, o_max)
        self.result = str(o_max)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask23ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

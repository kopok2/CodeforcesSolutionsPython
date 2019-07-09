class CodeforcesTask978ASolution:
    def __init__(self):
        self.result = ''
        self.elements_count = 0
        self.elements = []

    def read_input(self):
        self.elements_count = int(input())
        self.elements = [int(x) for x in input().split(" ")]

    def process_task(self):
        new_els = []
        rever = self.elements[::-1]
        for item in rever:
            if item not in new_els:
                new_els.append(item)
        self.result = "{0}\n{1}".format(len(new_els), " ".join([str(x) for x in new_els[::-1]]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask978ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

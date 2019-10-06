class CodeforcesTask847ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.cells = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.cells.append([int(y) for y in input().split(" ")])

    def process_task(self):
        lists = []
        for x in range(self.n):
            if not self.cells[x][0]:
                nc = [x + 1]
                curr = x
                while self.cells[curr][1]:
                    curr = self.cells[curr][1] - 1
                nc.append(curr + 1)
                lists.append(nc)
        for x in range(len(lists) - 1):
            self.cells[lists[x][1] - 1][1] = lists[x + 1][0]
            self.cells[lists[x + 1][0] - 1][0] = lists[x][1]
        self.result = "\n".join(["{0} {1}".format(*cell) for cell in self.cells])


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask847ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

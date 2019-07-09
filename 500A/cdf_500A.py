class CodeforcesTask500ASolution:
    def __init__(self):
        self.result = ''
        self.target = 0
        self.connections = []

    def read_input(self):
        self.target = int(input().split(" ")[1])
        self.connections = [int(x) for x in input().split(" ")]

    def process_task(self):
        targets = [x + self.connections[x] + 1 for x in range(len(self.connections))]
        if self.target not in targets:
            self.result = "NO"
        else:
            position = 1
            while position < self.target:
                position = targets[position - 1]
            if position == self.target:
                self.result = "YES"
            else:
                self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask500ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

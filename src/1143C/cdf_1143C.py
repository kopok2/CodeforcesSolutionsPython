class CodeforcesTask1143CSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.vertices = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.vertices.append([int(y) for y in input().split(" ")])

    def process_task(self):
        respected = {}
        for x in range(self.n):
            if not self.vertices[x][1]:
                respected[x + 1] = True
                respected[self.vertices[x][0]] = True
        result = []
        for x in range(self.n):
            if x + 1 not in respected:
                result.append(x + 1)
        self.result = " ".join([str(x) for x in result]) if result else "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1143CSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

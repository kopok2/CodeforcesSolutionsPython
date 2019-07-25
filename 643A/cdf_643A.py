class CodeforcesTask643ASolution:
    def __init__(self):
        self.result = ''
        self.ball_count = 0
        self.colors = []

    def read_input(self):
        self.ball_count = int(input())
        self.colors = [int(x) for x in input().split(" ")]

    def process_task(self):
        color_results = [0 for x in range(self.ball_count)]
        for x in range(self.ball_count):
            cl_counts = [0 for x in range(self.ball_count)]
            best = 0
            best_id = -1
            for y in range(x, self.ball_count):
                cl_counts[self.colors[y] - 1] += 1
                if cl_counts[self.colors[y] - 1] > best:
                    best = cl_counts[self.colors[y] - 1]
                    best_id = self.colors[y] - 1
                elif cl_counts[self.colors[y] - 1] == best:
                    if best_id > self.colors[y] - 1:
                        best_id = self.colors[y] - 1
                color_results[best_id] += 1
        self.result = " ".join([str(x) for x in color_results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask643ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

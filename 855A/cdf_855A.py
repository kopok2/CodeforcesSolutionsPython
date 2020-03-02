class CodeforcesTask855ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.diary = []

    def read_input(self):
        self.n = int(input())
        for _ in range(self.n):
            self.diary.append(input())

    def process_task(self):
        res = []
        visits = set()
        for entry in self.diary:
            if entry in visits:
                res.append("YES")
            else:
                res.append("NO")
                visits.add(entry)
        self.result = "\n".join(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask855ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

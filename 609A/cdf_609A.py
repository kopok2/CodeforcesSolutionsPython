class CodeforcesTask609ASolution:
    def __init__(self):
        self.result = ''
        self.pendrive_count = 0
        self.file_size = 0
        self.pendrives = []

    def read_input(self):
        self.pendrive_count = int(input())
        self.file_size = int(input())
        for x in range(self.pendrive_count):
            self.pendrives.append(int(input()))

    def process_task(self):
        self.pendrives.sort(reverse=True)
        p = 0
        cap = 0
        for pendrive in self.pendrives:
            p += 1
            cap += pendrive
            if cap >= self.file_size:
                break
        self.result = str(p)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask609ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

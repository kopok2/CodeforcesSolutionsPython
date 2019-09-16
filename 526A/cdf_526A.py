class CodeforcesTask526ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.level = ''

    def read_input(self):
        self.n = int(input())
        self.level = input()

    def process_task(self):
        can = False
        for y in range(1, self.n):
            for x in range(self.n - y - 1):
                do = True
                for z in range(5):
                    if x + z * y >= self.n:
                        do = False
                        break
                    if self.level[x + z * y] != "*":
                        do = False
                        break
                if do:
                    can = do
                    break
            if can:
                break
        self.result = "yes" if can else "no"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask526ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask527ASolution:
    def __init__(self):
        self.result = ''
        self.dims = []

    def read_input(self):
        self.dims = [int(x) for x in input().split(" ")]

    def process_task(self):
        i = 0
        a = self.dims[0]
        b = self.dims[1]
        while a != b:
            if a % b:
                i += a // b
                a = a % b
                if a < b:
                    swap = a
                    a = b
                    b = swap
            else:
                i += a // b
                break
        self.result = str(i)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask527ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

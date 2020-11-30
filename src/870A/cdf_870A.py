class CodeforcesTask870ASolution:
    def __init__(self):
        self.result = ''
        self.l1 = []
        self.l2 = []

    def read_input(self):
        input()
        self.l1 = input().split(" ")
        self.l2 = input().split(" ")

    def process_task(self):
        x = 1
        while True:
            in1 = False
            in2 = False
            for c in str(x):
                if c in self.l1:
                    in1 = True
                if c in self.l2:
                    in2 = True
            if in1 and in2:
                break
            x += 1
        self.result = str(x)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask870ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

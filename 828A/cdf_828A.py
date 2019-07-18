class CodeforcesTask828ASolution:
    def __init__(self):
        self.result = ''
        self.n_a_b = []
        self.groups = []

    def read_input(self):
        self.n_a_b = [int(x) for x in input().split(" ")]
        self.groups = [int(x) for x in input().split(" ")]

    def process_task(self):
        single = self.n_a_b[1]
        double = self.n_a_b[2]
        half = 0
        denials = 0
        for gr in self.groups:
            if gr == 2:
                if double:
                    double -= 1
                else:
                    denials += 2
            else:
                if single:
                    single -= 1
                elif double:
                    double -= 1
                    half += 1
                elif half:
                    half -= 1
                else:
                    denials += 1
        self.result = str(denials)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask828ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

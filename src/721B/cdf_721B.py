class CodeforcesTask721BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.passwords = []
        self.valid = ''

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        for x in range(self.n_k[0]):
            self.passwords.append(input())
        self.valid = input()

    def process_task(self):
        opt_pass = sum([1 for x in self.passwords if len(x) < len(self.valid)])
        pess_pass = sum([1 for x in self.passwords if len(x) <= len(self.valid)]) - 1
        opt_time = opt_pass + ((opt_pass // self.n_k[1]) * 5) + 1
        pess_time = pess_pass + ((pess_pass // self.n_k[1]) * 5) + 1
        self.result = "{0} {1}".format(opt_time, pess_time)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask721BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

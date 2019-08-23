class CodeforcesTask789BSolution:
    def __init__(self):
        self.result = ''
        self.b_q_l_m = []
        self.bad_numbers = []

    def read_input(self):
        self.b_q_l_m = [int(x) for x in input().split(" ")]
        self.bad_numbers = [int(x) for x in input().split(" ")]

    def process_task(self):
        term = self.b_q_l_m[0]
        q = self.b_q_l_m[1]
        terms_count = 0
        if q == 1 and term not in self.bad_numbers:
            if abs(term) <= self.b_q_l_m[2]:
                self.result = "inf"
            else:
                self.result = "0"
        elif q == 1:
            self.result = "0"
        elif q == 0:
            if abs(term) <= self.b_q_l_m[2]:
                if term not in self.bad_numbers:
                    terms_count += 1
                if 0 not in self.bad_numbers:
                    self.result = "inf"
                else:
                    self.result = str(terms_count)
            else:
                self.result = "0"
        elif q == -1:
            if term not in self.bad_numbers:
                if abs(term) <= self.b_q_l_m[2]:
                    self.result = "inf"
                else:
                    self.result = "0"
            else:
                if -term not in self.bad_numbers:
                    if abs(-term) <= self.b_q_l_m[2]:
                        self.result = "inf"
                    else:
                        self.result = "0"
                else:
                    self.result = "0"
        elif term == 0:
            if term not in self.bad_numbers:
                self.result = "inf"
            else:
                self.result = "0"
        else:
            while abs(term) <= self.b_q_l_m[2]:
                if term not in self.bad_numbers:
                    terms_count += 1
                term *= q
            self.result = str(terms_count)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask789BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

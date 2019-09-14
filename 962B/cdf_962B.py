class CodeforcesTask962BSolution:
    def __init__(self):
        self.result = ''
        self.n_a_b = []
        self.places = ''

    def read_input(self):
        self.n_a_b = [int(x) for x in input().split(" ")]
        self.places = input()

    def process_task(self):
        placement = [len(x) for x in self.places.split("*") if len(x) > 0]
        rema, remb = self.n_a_b[1], self.n_a_b[2]
        for p in placement:
            if not p % 2:
                rema -= p // 2
                remb -= p // 2
            else:
                if rema > remb:
                    rema -= p // 2 + 1
                    remb -= p // 2
                else:
                    rema -= p // 2
                    remb -= p // 2 + 1
            rema, remb = max(0, rema), max(0, remb)
        self.result = str(self.n_a_b[1] + self.n_a_b[2] - rema - remb)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask962BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

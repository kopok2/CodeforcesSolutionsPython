class CodeforcesTask289BSolution:
    def __init__(self):
        self.result = ''
        self.n_m_d = []
        self.matrix = []

    def read_input(self):
        self.n_m_d = [int(x) for x in input().split(" ")]
        for x in range(self.n_m_d[0]):
            self.matrix += [int(x) for x in input().split(" ")]

    def process_task(self):
        self.matrix.sort(reverse=True)
        #print(self.matrix)
        target = self.matrix[0]
        step = self.n_m_d[2]
        poss = True
        opers = []
        for x in range(1, len(self.matrix)):
            a = (target - self.matrix[x]) % step
            if a:
                poss = False
                break
            else:
                opers.append((target - self.matrix[x]) // step)
        if poss:
            #print(opers)
            if opers:
                a = round(len(opers) / 2) - 1
                if a < len(opers):
                    center_target = opers[a]
                else:
                    center_target = opers[a - 1]
                #print(center_target, round(len(opers) / 2) - 1)
                new_ops = [abs(x - center_target) for x in opers] + [center_target]
                #print(sum(new_ops), new_ops)
                self.result = str(sum(new_ops))
            else:
                self.result = "0"
        else:
            self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask289BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

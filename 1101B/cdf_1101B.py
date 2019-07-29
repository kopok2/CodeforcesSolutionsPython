class CodeforcesTask1101BSolution:
    def __init__(self):
        self.result = ''
        self.accordion = ''

    def read_input(self):
        self.accordion = input()

    def process_task(self):
        starts = self.accordion.split("[", 1)
        if len(starts) > 1:
            acc = starts[1]
            stops = acc[::-1].split("]", 1)
            if len(stops) > 1:
                inside = stops[1]
                if inside.count(":") < 2:
                    self.result = "-1"
                else:
                    acc_s = len(inside.split(":", 1)[0])
                    acc_e = len(inside[::-1].split(":", 1)[0])
                    if not acc_e:
                        acc_e = -len(inside)
                    #print(inside[acc_s:-acc_e])
                    acc_p = inside[acc_s:-acc_e].count("|")
                    #print(acc_s, acc_e, acc_p)
                    self.result = str(4 + acc_p)
            else:
                self.result = "-1"
            #print(stops)
        else:
            self.result = "-1"
        #print(starts)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1101BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

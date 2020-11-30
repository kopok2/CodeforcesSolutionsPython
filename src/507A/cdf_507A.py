from operator import itemgetter


class CodeforcesTask507ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.instruments = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.instruments = [int(x) for x in input().split(" ")]

    def process_task(self):
        instru = [(x + 1, self.instruments[x]) for x in range(self.n_k[0])]
        instru.sort(key=itemgetter(1))
        time = self.n_k[1]
        result = 0
        x = 0
        #print(instru)
        while time and x < self.n_k[0]:
            #print(time, instru[x][1])
            if time - instru[x][1] >= 0:
                result += 1

                time -= instru[x][1]
                x += 1
            else:
                time = 0
        self.result = "{0}\n{1}".format(result, " ".join([str(x) for x in [y[0] for y in instru[:result]]]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask507ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

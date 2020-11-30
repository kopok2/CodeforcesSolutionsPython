class CodeforcesTask107ASolution:
    def __init__(self):
        self.result = ''
        self.n_p = []
        self.pipes = []

    def read_input(self):
        self.n_p = [int(x) for x in input().split(" ")]
        for _ in range(self.n_p[1]):
            self.pipes.append([int(x) for x in input().split(" ")])

    def process_task(self):
        incomings = [[] for _ in range(self.n_p[0])]
        outcomings = [[] for _ in range(self.n_p[0])]
        for pipe in self.pipes:
            incomings[pipe[1] - 1].append(pipe[0])
            outcomings[pipe[0] - 1].append((pipe[1], pipe[2]))
        result = []
        for x in range(self.n_p[0]):
            if not incomings[x] and outcomings[x]:
                start = x + 1
                diam = outcomings[x][0][1]
                stop = outcomings[x][0][0]
                while outcomings[stop - 1]:
                    diam = min(diam, outcomings[stop - 1][0][1])
                    stop = outcomings[stop - 1][0][0]
                result.append(f"{start} {stop} {diam}")
        self.result = "{0}\n{1}".format(len(result), "\n".join(result))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask107ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

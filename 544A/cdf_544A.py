class CodeforcesTask544ASolution:
    def __init__(self):
        self.result = ''
        self.k = 0
        self.q = ''

    def read_input(self):
        self.k = int(input())
        self.q = input()

    def process_task(self):
        if len(set(list([ord(c) for c in self.q]))) < self.k:
            self.result = "NO"
        else:
            strings = []
            starts = set()
            for x in range(len(self.q)):
                if self.q[x] not in starts and len(starts) < self.k:
                    starts.add(self.q[x])
                    strings.append(self.q[x])
                else:
                    strings[-1] += self.q[x]
            self.result = "YES\n{0}".format("\n".join(strings))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask544ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

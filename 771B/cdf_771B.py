class CodeforcesTask771BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.notes = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.notes = input().split(" ")

    def process_task(self):
        names = [0] * self.n_k[0]
        for x in range(self.n_k[0] - self.n_k[1] + 1):
            if self.notes[x] == "NO":
                if not names[x]:
                    names[x] = x + 1
                    names[x + self.n_k[1] - 1] = x + 1
                else:
                    names[x + self.n_k[1] - 1] = names[x]
        nn = max(names) + 1
        for x in range(len(names)):
            if not names[x]:
                names[x] = nn
                nn += 1
        nn -= 1
        tna = [chr(ord("A") + x) for x in range(26)] + [chr(ord("A") + x) + chr(ord("a") + x) for x in range(26)] + [chr(ord("A") + x) + chr(ord("a") + x) * 2 for x in range(26)]
        #print(names, len(tna))
        self.result = " ".join([tna[x] for x in names])


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask771BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask790ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.effective = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.effective = [True if x == "YES" else False for x in input().split(" ")]

    def process_task(self):
        names = [None] * self.n_k[0]
        unique = 0
        for x in range(self.n_k[0] - self.n_k[1] + 1):
            if self.effective[x]:
                for y in range(self.n_k[1]):
                    if names[x + y] is None:
                        names[x + y] = unique
                        unique += 1
            else:
                names[x + self.n_k[1] - 1] = names[x]
        if names[0] is None:
            names[0] = 0
        #print(names)
        for x in range(self.n_k[0]):
            if names[x] is None:
                names[x] = names[x - 1]
        letters = "abcdefghijklmnops"

        named = [(a + b + c).capitalize() for a in letters for b in letters for c in letters]
        result = [named[x] for x in names]

        self.result = " ".join(result)

    def get_result(self):
        return self.result



if __name__ == "__main__":
    Solution = CodeforcesTask790ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

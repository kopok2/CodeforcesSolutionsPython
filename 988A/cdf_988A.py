class CodeforcesTask988ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.ratings = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.ratings = [int(x) for x in input().split(" ")]

    def process_task(self):
        unique_ratings = list(set(self.ratings))
        if len(unique_ratings) >= self.n_k[1]:
            self.result = "YES\n{0}".format(" ".join([str(self.ratings.index(x) + 1) for x in unique_ratings[:self.n_k[1]]]))
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask988ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

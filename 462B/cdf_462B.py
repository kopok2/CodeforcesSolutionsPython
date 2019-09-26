from operator import itemgetter


class CodeforcesTask462BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.cards = ''

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.cards = input()

    def process_task(self):
        scores = {}
        for c in self.cards:
            if c in scores:
                scores[c] += 1
            else:
                scores[c] = 1
        score = [(scores[c], c) for c in self.cards]
        score.sort(reverse=True)
        scorezs = {}
        for c in score[:self.n_k[1]]:
            if c[1] in scorezs:
                scorezs[c[1]] += 1
            else:
                scorezs[c[1]] = 1
        #print(scorezs, scores)
        scorez = [scorezs[x[1]] for x in score[:self.n_k[1]]]
        #print(score, scorez)
        self.result = str(sum(scorez))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask462BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

from operator import itemgetter


class CodeforcesTask74ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.participants = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.participants.append(input().split(" "))

    def process_task(self):
        scores = []
        for part in self.participants:
            score = 0
            score += int(part[1]) * 100
            score -= int(part[2]) * 50
            score += sum([int(x) for x in part[2:]])
            scores.append((part[0], score))
        scores.sort(reverse=True, key=itemgetter(1))
        self.result = scores[0][0]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask74ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

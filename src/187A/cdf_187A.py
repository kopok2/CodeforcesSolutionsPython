from operator import itemgetter


def to_remove(seq):
    i = 0
    #print(seq)
    prev = 0
    for x in range(1, len(seq)):

        if not seq[x] > seq[x-1]:
            i = x
            break
    if not i:
        i = len(seq)
    #print(len(seq), i)

    return len(seq) - i


class CodeforcesTask187ASolution:
    def __init__(self):
        self.result = ''
        self.sequence1 = []
        self.sequence2 = []

    def read_input(self):
        input()
        self.sequence1 = [int(x) for x in input().split(" ")]
        self.sequence2 = [int(x) for x in input().split(" ")]

    def process_task(self):
        seq_2 = [(i, x) for i, x in enumerate(self.sequence2)]
        seq_2 = sorted(seq_2, key=itemgetter(1))
        positions = [seq_2[self.sequence1[x] - 1][0] + 1 for x in range(len(self.sequence1))]
        #positions = [self.sequence2.index(self.sequence1[x]) + 1 for x in range(len(self.sequence1))]
        #print(positions == positions1)
        #print(positions1, positions)
        i = to_remove(positions)
        self.result = str(i)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask187ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

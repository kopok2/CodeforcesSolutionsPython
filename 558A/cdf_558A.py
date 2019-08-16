from operator import itemgetter


class CodeforcesTask558ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.trees = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.trees.append([int(x) for x in input().split(" ")])

    def process_task(self):
        left = [x for x in self.trees if x[0] < 0]
        right = [x for x in self.trees if x[0] > 0]
        left.sort(key=itemgetter(0), reverse=True)
        right.sort(key=itemgetter(0))
        left = [x[1] for x in left]
        right = [x[1] for x in right]
        collected = 0
        l_l = len(left)
        l_r = len(right)
        if l_l == l_r:
            collected = sum(left) + sum(right)
        elif l_l > l_r:
            if l_r:
                collected = sum(right) + sum(left[:l_r + 1])
            else:
                collected = left[0]
        else:
            if l_l:
                collected = sum(left) + sum(right[:l_l + 1])
            else:
                collected = right[0]
        self.result = str(collected)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask558ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask770BSolution:
    def __init__(self):
        self.result = ''
        self.x = 0

    def read_input(self):
        self.x = int(input())

    def process_task(self):
        ans = sum([int(c) for c in str(self.x)])
        ne = [int(x) for x in str(self.x)]
        ol = ne[::]
        for x in range(len(str(self.x))):
            #print(ol)
            if ol[-x - 1]:
                ne[-x - 1] -= 1
                for y in range(x):
                    ne[-y - 1] = 9
                if sum(ne) > ans:
                    ans = sum(ne)
                    ol = ne[::]
        self.result = str(int("".join([str(x) for x in ol])))



    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask770BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

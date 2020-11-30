class CodeforcesTask160BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.ticket = ''

    def read_input(self):
        self.n = int(input())
        self.ticket = input()

    def process_task(self):
        p1 = [int(x) for x in self.ticket[self.n:]]
        p2 = [int(x) for x in self.ticket[:self.n]]
        p1.sort()
        p2.sort()
        bij = True
        #print(p1, p2)
        for x in range(self.n):
            if p1[x] <= p2[x]:
                bij = False
                break
        #print(bij)
        if not bij:
            bij = True
            for x in range(self.n):
                if p1[x] >= p2[x]:
                    bij = False
                    break
        self.result = "YES" if bij else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask160BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

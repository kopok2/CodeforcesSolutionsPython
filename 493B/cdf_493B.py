class CodeforcesTask493BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.points = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.points.append(int(input()))

    def process_task(self):
        first = [x for x in self.points if x > 0]
        second = [-x for x in self.points if x < 0]
        f_points = sum(first)
        s_points = sum(second)
        if f_points > s_points:
            self.result = "first"
        elif f_points < s_points:
            self.result = "second"
        else:
            if len(first) > len(second) and first[:len(second)] == second:
                self.result = "first"
            elif len(first) < len(second) and first == second[:len(first)]:
                self.result = "second"
            else:
                x = 0
                while first[x] == second[x]:
                    x += 1
                    if x == len(first):
                        break
                if x == len(first):
                    if self.points[-1] > 0:
                        self.result = "first"
                    else:
                        self.result = "second"
                else:
                    if first[x] > second[x]:
                        self.result = "first"
                    else:
                        self.result = "second"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask493BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

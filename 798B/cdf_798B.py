class CodeforcesTask798BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.strings = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.strings.append(list(input()))

    def process_task(self):
        states = []
        for x in range(len(self.strings[0])):
            states.append("".join(self.strings[0][x:] + self.strings[0][:x]))
        to_be = set(states)
        can = True
        for string in self.strings:
            if "".join(string) not in to_be:
                can = False
                break
        if can:
            costs = {}
            for x in range(len(states)):
                if states[x] not in costs:
                    costs[states[x]] = x
            for string in self.strings[1:]:
                lstates = []
                for x in range(len(string)):
                    lstates.append("".join(string[x:] + string[:x]))
                lcosts = {}
                for x in range(len(lstates)):
                    if lstates[x] not in lcosts:
                        lcosts[lstates[x]] = x
                for key, value in lcosts.items():
                    costs[key] += value
            mn = 51 ** 2
            for key, value in costs.items():
                mn = min(mn, value)
            self.result = str(mn)
        else:
            self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask798BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

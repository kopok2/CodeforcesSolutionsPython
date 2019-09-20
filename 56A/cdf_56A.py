class CodeforcesTask56ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.clients = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.clients.append(input())

    def process_task(self):
        cnt = 0
        for x in range(self.n):
            try:
                j = int(self.clients[x])
                if j < 18:
                    cnt += 1
            except ValueError:
                if self.clients[x] in ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE",
                                        "TEQUILA", "VODKA", "WHISKEY", "WINE"]:
                    cnt += 1
        self.result = str(cnt)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask56ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

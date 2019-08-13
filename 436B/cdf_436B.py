class CodeforcesTask436BSolution:
    def __init__(self):
        self.result = ''
        self.n_m_k = []
        self.field = []

    def read_input(self):
        self.n_m_k = [int(x) for x in input().split(" ")]
        for x in range(self.n_m_k[0]):
            self.field.append(input())

    def process_task(self):
        result_row = [0 for x in range(self.n_m_k[1])]
        for x in range(self.n_m_k[0]):
            for y in range(self.n_m_k[1]):
                # print(x, y)
                field = self.field[x][y]
                if field == "R":
                    pos = y + x
                    if pos < self.n_m_k[1]:
                        result_row[pos] += 1
                elif field == "L":
                    pos = y - x
                    if pos >= 0:
                        result_row[pos] += 1
                elif field == "U" and not x % 2:
                    result_row[y] += 1
        self.result = " ".join([str(x) for x in result_row])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask436BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

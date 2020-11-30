class CodeforcesTask486BSolution:
    def __init__(self):
        self.result = ''
        self.m_n = []
        self.matrix = []

    def read_input(self):
        self.m_n = [int(x) for x in input().split(" ")]
        for x in range(self.m_n[0]):
            self.matrix.append([int(y) for y in input().split(" ")])

    def process_task(self):
        rows = [sum(row) == self.m_n[1] for row in self.matrix]
        cols = [False] * self.m_n[1]
        for x in range(self.m_n[1]):
            col = 0
            for y in range(self.m_n[0]):
                col += self.matrix[y][x]
            if col == self.m_n[0]:
                cols[x] = True
        can = True
        #print(rows, cols)
        for x in range(self.m_n[0]):
            for y in range(self.m_n[1]):
                if self.matrix[x][y]:
                    if not (rows[x] or cols[y]):
                        # print(x, y, rows, cols)
                        can = False
                        break
            if not can:
                break
        if (sum([1 if x else 0 for x in cols]) and not sum([1 if x else 0 for x in rows])) or \
                (sum([1 if x else 0 for x in rows]) and not sum([1 if x else 0 for x in cols])):
           can = False
        if can:
            new_matrix = []
            for y in range(self.m_n[0]):
                row = []
                for x in range(self.m_n[1]):
                    row.append(1 if rows[y] and cols[x] else 0)
                new_matrix.append(row)
            self.result = "YES\n{0}".format("\n".join([" ".join([str(x) for x in row]) for row in new_matrix]))
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask486BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

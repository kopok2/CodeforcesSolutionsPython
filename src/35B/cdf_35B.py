class CodeforcesTask35BSolution:
    def __init__(self):
        self.result = ''
        self.n_m_k = []
        self.queries = []

    def read_input(self):
        with open("input.txt", "r") as in_file:
            in_data = in_file.readlines()
            self.n_m_k = [int(x) for x in in_data[0].strip().split(" ")]
            self.queries = [[x for x in query.strip().split(" ")] for query in in_data[1:]]

    def process_task(self):
        warehouse = [['' for x in range(self.n_m_k[1])] for y in range(self.n_m_k[0])]

        with open("output.txt", "w") as outfile:
            for query in self.queries:
                if query[0] == "+1":
                    put = False
                    posx = int(query[2]) - 1
                    posy = int(query[1]) - 1
                    while not put:
                        if not warehouse[posy][posx]:
                            put = True
                            warehouse[posy][posx] = query[3]
                        else:
                            posx += 1
                            if posx >= self.n_m_k[1]:
                                posx = 0
                                posy += 1
                                if posy >= self.n_m_k[0]:
                                    put = True
                else:
                    got = False
                    for y in range(self.n_m_k[0]):
                        for x in range(self.n_m_k[1]):
                            if warehouse[y][x] == query[1]:
                                got = True
                                outfile.write("{0} {1}\n".format(y + 1, x + 1))
                                warehouse[y][x] = ""
                                break
                    if not got:
                        outfile.write("-1 -1\n")

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask35BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

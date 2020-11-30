class CodeforcesTask475ASolution:
    def __init__(self):
        self.result = ''
        self.passengers = 0

    def read_input(self):
        self.passengers = int(input())

    def process_task(self):
        seats = ["#" for x in range(34)]
        for x in range(self.passengers):
            seats[x] = "O"
        bus = """+------------------------+
|{0}.{4}.{7}.{10}.{13}.{16}.{19}.{22}.{25}.{28}.{31}.|D|)
|{1}.{5}.{8}.{11}.{14}.{17}.{20}.{23}.{26}.{29}.{32}.|.|
|{2}.......................|
|{3}.{6}.{9}.{12}.{15}.{18}.{21}.{24}.{27}.{30}.{33}.|.|)
+------------------------+""".format(*seats)
        self.result = bus

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask475ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

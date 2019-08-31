class CodeforcesTask794ASolution:
    def __init__(self):
        self.result = ''
        self.a_b_c = []
        self.n = 0
        self.banknotes = []

    def read_input(self):
        self.a_b_c = [int(x) for x in input().split(" ")]
        self.n = int(input())
        self.banknotes = [int(x) for x in input().split(" ")]

    def process_task(self):
        notes = 0
        for note in self.banknotes:
            if self.a_b_c[1] < note < self.a_b_c[2]:
                notes += 1
        self.result = str(notes)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask794ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

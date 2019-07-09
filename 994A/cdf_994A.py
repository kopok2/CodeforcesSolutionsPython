class CodeforcesTask994ASolution:
    def __init__(self):
        self.sequence = []
        self.fingerprints = []
        self.result = ""

    def read_input(self):
        input()
        self.sequence = input().split(" ")
        self.fingerprints = input().split(" ")

    def process_task(self):
        for number in self.sequence:
            if number in self.fingerprints:
                self.result += " {0}".format(number)

    def get_result(self):
        return self.result[1:]


if __name__ == "__main__":
    Solution = CodeforcesTask994ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

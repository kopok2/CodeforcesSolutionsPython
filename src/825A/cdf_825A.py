class CodeforcesTask825ASolution:
    def __init__(self):
        self.result = ''
        self.encoded = ''

    def read_input(self):
        input()
        self.encoded = input()

    def process_task(self):
        res = [len(x) for x in self.encoded.split("0")]
        self.result = "".join([str(x) for x in res])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask825ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

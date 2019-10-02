class CodeforcesTask710ASolution:
    def __init__(self):
        self.result = ''
        self.position = ''

    def read_input(self):
        self.position = input()

    def process_task(self):
        if self.position in ['a8', 'a1', 'h8', 'h1']:
            self.result = "3"
        elif self.position[0] in 'ah' or self.position[1] in '18':
            self.result = "5"
        else:
            self.result = "8"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask710ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

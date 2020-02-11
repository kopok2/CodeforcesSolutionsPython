class CodeforcesTask216ASolution:
    def __init__(self):
        self.result = ''
        self.a_b_c = []

    def read_input(self):
        self.a_b_c = [int(x) for x in input().split(" ")]

    def process_task(self):
        result = 0
        a, b, c = self.a_b_c
        width = a
        for step in range(1, b + c):

            result += width
            if step < b and step < c:
                width += 1
            elif step >= b and step >= c:
                width -= 1
        self.result = str(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask216ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

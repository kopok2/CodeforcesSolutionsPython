class CodeforcesTask784ASolution:
    def __init__(self):
        self.result = ''
        self.a = 0

    def read_input(self):
        self.a = int(input())

    def process_task(self):
        self.result = str([4, 22, 27, 58, 85, 94, 121, 166, 202, 265, 274, 319, 346, 355, 378, 382, 391, 438, 454, 483, 517, 526, 535, 562, 576, 588, 627, 634, 636, 645, 648, 654, 663, 666, 690, 706, 728, 729, 762, 778, 825, 852, 861, 895, 913, 915, 922, 958, 985, 1086, 1111, 1165][self.a - 1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask784ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

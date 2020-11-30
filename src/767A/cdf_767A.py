class CodeforcesTask767ASolution:
    def __init__(self):
        self.result = ''
        self.part_count = 0
        self.parts = []

    def read_input(self):
        self.part_count = int(input())
        self.parts = [int(x) for x in input().split(" ")]

    def process_task(self):
        ava_parts = [False for x in range(self.part_count)]
        level = self.part_count
        for i, part in enumerate(self.parts):
            ava_parts[part-1] = True
            for x in range(level, 0, -1):
                if ava_parts[x-1]:
                    print(str(x), end=" ")
                    ava_parts[x-1] = False
                    level -= 1
                else:
                    break

            print("\n", end="")

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask767ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

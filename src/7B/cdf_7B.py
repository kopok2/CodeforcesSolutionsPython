from operator import itemgetter


class CodeforcesTask7BSolution:
    def __init__(self):
        self.result = ''
        self.t_m = []
        self.commands = []

    def read_input(self):
        self.t_m = [int(x) for x in input().split(" ")]
        for x in range(self.t_m[0]):
            self.commands.append(input().split(" "))

    def process_task(self):
        results = []
        memory = [(0, self.t_m[1], 0, self.t_m[1])]
        try:
            for cmd in self.commands:
                max_empty =
                if cmd[0] == "alloc":

                elif cmd[0] == "erase":

                else:

        except Exception as e:
            print(e)
        self.result = "\n".join([str(x) for x in results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask7BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

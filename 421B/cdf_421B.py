class CodeforcesTask421BSolution:
    def __init__(self):
        self.result = ''
        self.name = ''

    def read_input(self):
        self.name = input()

    def process_task(self):
        symetric = "AHIMOTUVWXY"
        origin = self.name[len(self.name) // 2 + len(self.name) % 2 - 1:]
        mirror = self.name[::-1][len(self.name) // 2 + len(self.name) % 2 - 1:]
        #if "VAAOWHUOTHTHHYOAIAYUXI" in self.name:
        #    print(origin[:50], mirror[:50])
        if origin != mirror:
            self.result = "NO"
        else:
            can_ = True
            for c in self.name:
                if c not in symetric:
                    can_ = False
                    break
            self.result = "YES" if can_ else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask421BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

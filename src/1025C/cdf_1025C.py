def zebra_len(zebra):
    l = 1
    c = 0
    p = "x"
    for z in zebra:
        if (p == "w" and z == "b") or (p == "b" and z == "w"):
            c += 1
            l = max(l, c)
        else:
            c = 1
        p = z
    return l


class CodeforcesTask1025CSolution:
    def __init__(self):
        self.result = ''
        self.zebra = ''

    def read_input(self):
        self.zebra = input()

    def process_task(self):
        self.result = str(min(len(self.zebra), zebra_len(self.zebra * 2)))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1025CSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

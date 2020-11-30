from collections import Counter


class CodeforcesTask43BSolution:
    def __init__(self):
        self.result = ''
        self.s1 = ''
        self.s2 = ''

    def read_input(self):
        self.s1 = input().replace(" ", "")
        self.s2 = input().replace(" ", "")

    def process_task(self):
        avail = Counter(self.s1)
        needed = Counter(self.s2)
        can = True
        for key in needed.keys():
            if key in avail:
                if avail[key] < needed[key]:
                    can = False
                    break
            else:
                can = False
                break
        self.result = "YES" if can else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask43BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

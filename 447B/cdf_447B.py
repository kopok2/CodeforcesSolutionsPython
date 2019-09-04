class CodeforcesTask447BSolution:
    def __init__(self):
        self.result = ''
        self.string = ''
        self.k = 0
        self.values = []

    def read_input(self):
        self.string = input()
        self.k = int(input())
        self.values = [int(x) for x in input().split(" ")]

    def process_task(self):
        values = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for x in range(len(alphabet)):
            values[alphabet[x]] = self.values[x]
        total_value = 0
        mx_val = max(self.values)
        for i in range(len(self.string)):
            total_value += (i + 1) * values[self.string[i]]
        for i in range(len(self.string), len(self.string) + self.k):
            total_value += (i + 1) * mx_val
        self.result = str(total_value)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask447BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

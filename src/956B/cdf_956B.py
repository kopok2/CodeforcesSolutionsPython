def ece(k, i, j):
    return (k - j) / (k - i)


def binary_search(array, value):
    left = 0
    right = len(array) - 1
    while right - left:
        mid = left + ((right - left) // 2)
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            right = mid
        else:
            left = mid
        if right - left == 1:
            left = right
            mid = left + ((right - left) // 2)
            if array[mid] == value:
                return mid
            if array[mid - 1] == value:
                return mid - 1
    return right


class CodeforcesTask956BSolution:
    def __init__(self):
        self.result = ''
        self.n_u = []
        self.states = []

    def read_input(self):
        self.n_u = [int(x) for x in input().split(" ")]
        self.states = [int(x) for x in input().split(" ")]

    def process_task(self):
        rates = []
        for x in range(self.n_u[0] - 2):
            blc = binary_search(self.states, self.states[x] + self.n_u[1])
            # print(self.states[x], self.states[x] + self.n_u[1], blc, x, blc - x, self.states[blc])
            if self.states[blc] > self.states[x] + self.n_u[1]:
                blc -= 1
            if blc - x > 1:
                rates.append(ece(self.states[blc], self.states[x], self.states[x + 1]))
        # print(rates)
        if not rates:
            self.result = "-1"
        else:
            self.result = str(max(rates))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask956BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

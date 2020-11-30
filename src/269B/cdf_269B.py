global maximum


def longest_increasing_subsequence(array, n):
    global maximum
    if n == 1:
        return 1
    max_ending = 1
    for i in range(1, n):
        res = longest_increasing_subsequence(array, i)
        if array[i - 1] <= array[n - 1] and res + 1 > max_ending:
            max_ending = res + 1
    maximum = max(maximum, max_ending)
    return max_ending

def lis(array):
    global maximum
    maximum = 1
    longest_increasing_subsequence(array, len(array))
    return maximum

class CodeforcesTask269BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.plants = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.plants.append([float(y) for y in input().split(" ")])

    def process_task(self):
        ar = [int(x[0]) for x in self.plants]
        self.result = str(self.n_m[0] - lis(ar))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask269BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

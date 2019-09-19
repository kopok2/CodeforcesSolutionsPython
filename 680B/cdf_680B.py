class CodeforcesTask680BSolution:
    def __init__(self):
        self.result = ''
        self.n_a = []
        self.cities = []

    def read_input(self):
        self.n_a = [int(x) for x in input().split(" ")]
        self.cities = [int(x) for x in input().split(" ")]

    def process_task(self):
        catch_cnt = 0
        p = self.n_a[1]
        r = 0
        while p + r <= self.n_a[0] or p - r >= 1:
            if p + r <= self.n_a[0] and p - r >= 1:
                if self.cities[p + r - 1] == self.cities[p - r - 1]:
                    if p + r - 1 == p - r - 1:
                        catch_cnt += 1 * self.cities[p + r - 1]
                    else:
                        catch_cnt += 2 * self.cities[p + r - 1]
            elif p + r <= self.n_a[0]:
                if self.cities[p + r - 1]:
                    catch_cnt += 1
            elif p - r >= 1:
                if self.cities[p - r - 1]:
                    catch_cnt += 1
            r += 1
        self.result = str(catch_cnt)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask680BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

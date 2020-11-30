def is_prime(number):
    result = True
    for x in range(2, number):
        if not number % x:
            result = False
            break
    return result


class CodeforcesTask755ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        for m in range(1, 1000):
            if not is_prime(m*self.n + 1):
                self.result = str(m)
                break

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask755ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

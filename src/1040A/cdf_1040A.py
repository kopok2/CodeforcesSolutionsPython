def can_form_palindrome(dancers):
    result = True
    for x in range(len(dancers)):
        if dancers[x] == 1 and dancers[len(dancers)-x-1] == 0 or dancers[x] == 0 and dancers[len(dancers)-x-1] == 1:
            result = False
    return result


class CodeforcesTask1040ASolution:
    def __init__(self):
        self.result = ''
        self.n_a_b = []
        self.dancers = []

    def read_input(self):
        self.n_a_b = [int(x) for x in input().split(" ")]
        self.dancers = [int(x) for x in input().split(" ")]

    def process_task(self):
        if can_form_palindrome(self.dancers):
            preffered = min(self.n_a_b[1], self.n_a_b[2])
            price = 0
            for x in range(len(self.dancers)):
                if self.dancers[x] == 2 and self.dancers[len(self.dancers) - x - 1] == 2:
                    price += preffered
                if self.dancers[x] == 0 and self.dancers[len(self.dancers) - x - 1] == 2 or \
                   self.dancers[x] == 2 and self.dancers[len(self.dancers) - x - 1] == 0:
                    price += self.n_a_b[1] / 2
                if self.dancers[x] == 1 and self.dancers[len(self.dancers) - x - 1] == 2 or \
                   self.dancers[x] == 2 and self.dancers[len(self.dancers) - x - 1] == 1:
                    price += self.n_a_b[2] / 2
            self.result = str(int(price))

        else:
            self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1040ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

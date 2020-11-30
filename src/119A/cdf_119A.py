import math


class CodeforcesTask119ASolution:
    def __init__(self):
        self.result = ''
        self.a_b_n = []

    def read_input(self):
        self.a_b_n = [int(x) for x in input().split(" ")]

    def process_task(self):
        turn = 0
        while True:
            #print(self.a_b_n, turn)
            if not turn:
                if math.gcd(self.a_b_n[0], self.a_b_n[2]) <= self.a_b_n[2]:
                    self.a_b_n[2] -= math.gcd(self.a_b_n[0], self.a_b_n[2])
                else:
                    winner = 1
                    break
                turn = 1
            else:
                if math.gcd(self.a_b_n[1], self.a_b_n[2]) <= self.a_b_n[2]:
                    self.a_b_n[2] -= math.gcd(self.a_b_n[1], self.a_b_n[2])
                else:
                    winner = 0
                    break
                turn = 0
        self.result = str(winner)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask119ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

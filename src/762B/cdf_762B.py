from collections import deque


class CodeforcesTask762BSolution:
    def __init__(self):
        self.result = ''
        self.a_b_c = []
        self.m = 0
        self.prices = []

    def read_input(self):
        self.a_b_c = [int(x) for x in input().split(" ")]
        self.m = int(input())
        for _ in range(self.m):
            self.prices.append(input().split(" "))
            self.prices[-1][0] = int(self.prices[-1][0])
            self.prices[-1][1] = 0 if self.prices[-1][1] == "USB" else 1

    def process_task(self):
        prices1 = [x[0] for x in self.prices if not x[1]]
        prices2 = [x[0] for x in self.prices if x[1]]
        prices1.sort()
        prices2.sort()
        equipped = 0
        cost = 0
        prices1 = deque(prices1)
        prices2 = deque(prices2)
        while prices1 and self.a_b_c[0]:
            equipped += 1
            cost += prices1.popleft()
            #print(cost)
            self.a_b_c[0] -= 1
        while prices2 and self.a_b_c[1]:
            equipped += 1
            cost += prices2.popleft()
            #print(cost)
            self.a_b_c[1] -= 1
        while (prices1 or prices2) and self.a_b_c[2]:
            equipped += 1
            self.a_b_c[2] -= 1
            if prices1 and prices2:
                if prices1[0] <= prices2[0]:
                    cost += prices1.popleft()
                else:
                    cost += prices2.popleft()
            elif prices1:
                cost += prices1.popleft()
            else:
                cost += prices2.popleft()
            #print(cost)
        self.result = f"{equipped} {cost}"



    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask762BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

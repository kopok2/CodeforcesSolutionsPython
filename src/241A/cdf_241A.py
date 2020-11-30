import math


class CodeforcesTask241ASolution:
    def __init__(self):
        self.result = ''
        self.m_k = []
        self.distances = []
        self.supplies = []

    def read_input(self):
        self.m_k = [int(x) for x in input().split(" ")]
        self.distances = [int(x) for x in input().split(" ")]
        self.supplies = [int(x) for x in input().split(" ")]

    def process_task(self):
        travel_time = sum(self.distances)
        position = 0
        fuel = self.supplies[0]
        max_supply = self.supplies[0]
        while position < self.m_k[0]:
            if fuel >= self.distances[position]:
                fuel -= self.distances[position]
                position += 1
                if position == self.m_k[0]:
                    break
                fuel += self.supplies[position]
                max_supply = max(max_supply, self.supplies[position])
            else:
                tanking = self.distances[position] - fuel
                tanking_rounds = tanking // max_supply + int(math.ceil(tanking % max_supply / max_supply))
                fuel += tanking_rounds * max_supply
                travel_time += tanking_rounds * self.m_k[1]
        self.result = str(travel_time)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask241ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

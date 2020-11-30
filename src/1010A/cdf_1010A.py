def flight_cost(mass, cost):
    return mass / (cost - 1)


class CodeforcesTask1010ASolution:
    def __init__(self):
        self.result = ''
        self.planet_count = 0
        self.payload = 0
        self.takeoff_costs = []
        self.landing_costs = []

    def read_input(self):
        self.planet_count = int(input())
        self.payload = int(input())
        self.takeoff_costs = [int(x) for x in input().split(" ")]
        self.landing_costs = [int(x) for x in input().split(" ")]

    def process_task(self):
        try:
            payload = self.payload
            required_fuel = 0
            nf = flight_cost(payload, self.landing_costs[0])
            required_fuel += nf
            payload += nf
            for x in range(1, self.planet_count):
                nf = flight_cost(payload, self.takeoff_costs[self.planet_count - x])
                required_fuel += nf
                payload += nf
                nf = flight_cost(payload, self.landing_costs[self.planet_count - x])
                required_fuel += nf
                payload += nf
                # print(self.planet_count - x - 1)
            nf = flight_cost(payload, self.takeoff_costs[0])
            required_fuel += nf
            payload += nf
            self.result = str(required_fuel)
        except ZeroDivisionError:
            self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1010ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

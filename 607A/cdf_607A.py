class CodeforcesTask607ASolution:
    def __init__(self):
        self.result = ''
        self.beacons_count = 0
        self.beacons = [0 for x in range(1000005)]

    def read_input(self):
        self.beacons_count = int(input())
        for x in range(self.beacons_count):
            a_b = ([int(x) for x in input().split(" ")])
            self.beacons[a_b[0]] = a_b[1]

    def process_task(self):
        dp = [0 for x in range(1000005)]
        for x in range(len(self.beacons)):
            if self.beacons[x]:
                dp[x] = 1
        mx = 0
        for x in range(1, 1000005):
            if not self.beacons[x]:
                dp[x] = dp[x - 1]
            else:
                if self.beacons[x] >= x:
                    dp[x] = 1
                else:
                    dp[x] = dp[x - self.beacons[x] - 1] + 1
            if dp[x] > mx:
                mx = dp[x]
        self.result = str(self.beacons_count - mx)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask607ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask920ASolution:
    def __init__(self):
        self.result = ''
        self.test_cases = 0

    def read_input(self):
        self.test_cases = int(input())

    def process_task(self):
        for test in range(self.test_cases):
            n_k = [int(x) for x in input().split(" ")]
            taps = [int(x) for x in input().split(" ")]
            positioned_taps = [1 if x + 1 in taps else 0 for x in range(n_k[0])]
            forward_tap = [-1 for x in range(n_k[0])]
            backward_tap = [-1 for x in range(n_k[0])]

            last_f = -1
            for x in range(n_k[0]):
                if positioned_taps[x]:
                    last_f = x
                if last_f >= 0:
                    forward_tap[x] = abs(x - last_f) + 1
            last_b = -1
            for x in range(n_k[0] - 1, -1, -1):
                if positioned_taps[x]:
                    last_b = x
                if last_b >= 0:
                    backward_tap[x] = abs(x - last_b) + 1
            tapping = [0 for x in range(n_k[0])]
            for x in range(n_k[0]):
                if forward_tap[x] == -1:
                    tapping[x] = backward_tap[x]
                elif backward_tap[x] == -1:
                    tapping[x] = forward_tap[x]
                else:
                    tapping[x] = min(forward_tap[x], backward_tap[x])
            print(max(tapping))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask920ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

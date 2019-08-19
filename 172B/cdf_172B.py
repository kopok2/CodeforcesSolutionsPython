def rand(a, b, m, r):
    return (a * r + b) % m


class CodeforcesTask172BSolution:
    def __init__(self):
        self.result = ''
        self.a_b_m_r = []

    def read_input(self):
        self.a_b_m_r = [int(x) for x in input().split(" ")]

    def process_task(self):
        sequence = [rand(*self.a_b_m_r)]
        for x in range(100000):
            sequence.append(rand(self.a_b_m_r[0], self.a_b_m_r[1], self.a_b_m_r[2], sequence[-1]))
        freq = []
        counts = [0 for x in range(max(sequence) + 1)]
        for s in sequence:
            counts[s] += 1
        #print(sequence)
        for x in list(set(sequence)):
            freq.append((x, round(10000 * (counts[x] / len(sequence)))))

        #print(freq)
        cycle = 0
        cycle_r = max([x[1] for x in freq])
        for f in freq:
            #print(f)
            if abs(f[1] - cycle_r) <= 2:
                cycle += 1
        #print(cycle_r)
        self.result = str(cycle)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask172BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask321ASolution:
    def __init__(self):
        self.result = ''
        self.a_b = []
        self.command = ''

    def read_input(self):
        self.a_b = [int(x) for x in input().split(" ")]
        self.command = input()

    def process_task(self):
        vector = [0, 0]
        for c in self.command:
            if c == "U":
                vector[1] += 1
            elif c == "D":
                vector[1] -= 1
            elif c == "R":
                vector[0] += 1
            elif c == "L":
                vector[0] -= 1
        if vector[0] and vector[1]:
            turns_away = min(self.a_b[0] // vector[0], self.a_b[1] // vector[1])
        elif vector[0]:
            turns_away = self.a_b[0] // vector[0]
        elif vector[1]:
            turns_away = self.a_b[1] // vector[1]
        else:
            turns_away = 0
        turns_away = max(turns_away - 50, 0)
        x = vector[0] * turns_away
        y = vector[1] * turns_away
        can = False
        #print(vector, turns_away, x, y)
        if x == self.a_b[0] and y == self.a_b[1]:
            can = True
        for z in range(100):
            for c in self.command:
                if c == "U":
                    y += 1
                elif c == "D":
                    y -= 1
                elif c == "R":
                    x += 1
                elif c == "L":
                    x -= 1
                if x == self.a_b[0] and y == self.a_b[1]:
                    can = True
        self.result = "Yes" if can else "No"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask321ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

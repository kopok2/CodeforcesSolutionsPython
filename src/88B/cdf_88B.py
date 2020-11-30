import math


def dist(a, b, c, d):
    return math.sqrt((a - c) ** 2 + (b - d) ** 2)


class CodeforcesTask88BSolution:
    def __init__(self):
        self.result = ''
        self.n_m_x = []
        self.keyboard = []
        self.text = ""

    def read_input(self):
        self.n_m_x = [int(x) for x in input().split(" ")]
        for x in range(self.n_m_x[0]):
            self.keyboard.append(input())
        input()
        self.text = input()

    def process_task(self):
        alphabet = {}
        getcha_shift = False
        for x in range(self.n_m_x[0]):
            for y in range(self.n_m_x[1]):
                if self.keyboard[x][y] != "S":
                    alphabet[self.keyboard[x][y]] = True
                else:
                    getcha_shift = True
                    for a in range(x - self.n_m_x[2], x + self.n_m_x[2] + 1):
                        if -1 < a < self.n_m_x[0]:
                            for b in range(y - self.n_m_x[2], y + self.n_m_x[2] + 1):
                                if -1 < b < self.n_m_x[1]:
                                    if self.keyboard[a][b] != "S":
                                        if dist(a, b, x, y) <= self.n_m_x[2]:
                                            alphabet[self.keyboard[a][b].upper()] = True
        bad_alpha = {}
        if getcha_shift:
            for key in alphabet.keys():
                bad_alpha[key.upper()] = True
        canbe = True
        strokes = 0
        #print(alphabet, bad_alpha)
        for c in self.text:
            if c not in alphabet:
                if c in bad_alpha:
                    strokes += 1
                else:
                    canbe = False
                    break
        if canbe:
            self.result = str(strokes)
        else:
            self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask88BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

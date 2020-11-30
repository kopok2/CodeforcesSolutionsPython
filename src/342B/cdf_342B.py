import math


def locked(x, a, b):
    return a <= x <= b


class CodeforcesTask342BSolution:
    def __init__(self):
        self.result = ''
        self.n_m_s_f = []
        self.controls = []

    def read_input(self):
        self.n_m_s_f = [int(x) for x in input().split(" ")]

    def process_task(self):
        move = ''
        pos = self.n_m_s_f[2]
        direction = int(math.copysign(1, self.n_m_s_f[3] - self.n_m_s_f[2]))
        #print(direction)
        move_char = "L" if direction < 0 else "R"
        turn = 1
        controls_left = self.n_m_s_f[1] - 1
        control = [int(x) for x in input().split(" ")]
        c_turn = control[0]
        a = control[1]
        b = control[2]
        while not pos == self.n_m_s_f[3]:
            #print(pos, turn)
            if c_turn == turn:
                if not locked(pos, a, b) and not locked(pos + direction, a, b):
                    move += move_char
                    pos += direction
                else:
                    move += "X"
                if controls_left:
                    controls_left -= 1
                    control = [int(x) for x in input().split(" ")]
                    c_turn = control[0]
                    a = control[1]
                    b = control[2]

            else:
                move += move_char
                pos += direction
            turn += 1
            if len(move) > 400:
                print(move, end="")
                move = ''
        for x in range(controls_left):
            input()
        print(move, end="")

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask342BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

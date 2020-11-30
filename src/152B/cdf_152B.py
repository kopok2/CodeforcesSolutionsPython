def make_step(x, y, n, m, vector):
    if vector[0] > 0:
        if vector[1] > 0:
            mx_step_x = (n - x) // vector[0]
            mx_step_y = (m - y) // vector[1]
            made_steps = min(mx_step_x, mx_step_y)
            if made_steps < 0:
                print("NO way 1", x, y, n, m , vector)
            return x + vector[0] * made_steps, y + vector[1] * made_steps, made_steps
        elif vector[1] == 0:
            made_steps = (n - x) // vector[0]
            if made_steps < 0:
                print("NO way 2", x, y, n, m , vector)
            return x + vector[0] * made_steps, y, made_steps
        else:
            mx_step_x = (n - x) // vector[0]
            mx_step_y = (y - 1) // -vector[1]
            made_steps = min(mx_step_x, mx_step_y)
            if made_steps < 0:
                print("NO way 3", x, y, n, m , vector)
            return x + vector[0] * made_steps, y + vector[1] * made_steps, made_steps
    elif vector[0] == 0:
        if vector[1] > 0:
            made_steps = (m - y) // vector[1]
            if made_steps < 0:
                print("NO way 4", x, y, n, m , vector)
            return x, y + made_steps * vector[1], made_steps
        elif vector[1] == 0:
            return x, y, 0
        else:
            made_steps = (y - 1) // -vector[1]
            if made_steps < 0:
                print("NO way 5", x, y, n, m , vector)
            return x, y + made_steps * vector[1], made_steps
    else:
        if vector[1] > 0:
            mx_step_x = (x - 1) // -vector[0]
            mx_step_y = (m - y) // vector[1]
            made_steps = min(mx_step_x, mx_step_y)
            if made_steps < 0:
                print("NO way 6", x, y, n, m , vector)
            return x + vector[0] * made_steps, y + vector[1] * made_steps, made_steps
        elif vector[1] == 0:
            made_steps = (x - 1) // -vector[0]
            if made_steps < 0:
                print("NO way 7", x, y, n, m , vector)
            return x + vector[0] * made_steps, y, made_steps
        else:
            mx_step_x = (x - 1) // -vector[0]
            mx_step_y = (y - 1) // -vector[1]
            made_steps = min(mx_step_x, mx_step_y)
            if made_steps < 0:
                print("NO way 8", x, y, n, m , vector)
            return x + vector[0] * made_steps, y + vector[1] * made_steps, made_steps


class CodeforcesTask152BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.x_y = []
        self.k = 0
        self.vectors = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.x_y = [int(x) for x in input().split(" ")]
        self.k = int(input())
        for x in range(self.k):
            self.vectors.append([int(y) for y in input().split(" ")])

    def process_task(self):
        x_pos, y_pos = self.x_y
        steps = 0
        for vector in self.vectors:
            x_pos, y_pos, new_steps = make_step(x_pos, y_pos, *self.n_m, vector)
            #print(new_steps, x_pos, y_pos, vector)
            steps += new_steps
        self.result = str(steps)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask152BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

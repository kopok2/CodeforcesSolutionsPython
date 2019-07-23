class CodeforcesTask459ASolution:
    def __init__(self):
        self.result = ''
        self.cords = []

    def read_input(self):
        self.cords = [int(x) for x in input().split(" ")]

    def process_task(self):
        x_dist = abs(self.cords[0] - self.cords[2])
        y_dist = abs(self.cords[1] - self.cords[3])
        top_right = [0, 0]
        top_left = [0, 0]
        bottom_right = [0, 0]
        bottom_left = [0, 0]
        if x_dist and y_dist:
            if x_dist == y_dist:
                a = x_dist
            else:
                self.result = "-1"
        else:
            if x_dist:
                a = x_dist
            else:
                a = y_dist
        if not self.result:
            if x_dist and y_dist:
                bottom_left[0] = min(self.cords[0], self.cords[2])
                bottom_left[1] = min(self.cords[1], self.cords[3])
                bottom_right[0] = max(self.cords[0], self.cords[2])
                bottom_right[1] = min(self.cords[1], self.cords[3])
                top_left[0] = min(self.cords[0], self.cords[2])
                top_left[1] = max(self.cords[1], self.cords[3])
                top_right[0] = max(self.cords[0], self.cords[2])
                top_right[1] = max(self.cords[1], self.cords[3])
            elif x_dist:
                bottom_left[0] = min(self.cords[0], self.cords[2])
                bottom_left[1] = min(self.cords[1], self.cords[3])
                bottom_right[0] = max(self.cords[0], self.cords[2])
                bottom_right[1] = min(self.cords[1], self.cords[3])
                top_left[0] = min(self.cords[0], self.cords[2])
                top_left[1] = self.cords[1] + a
                top_right[0] = max(self.cords[0], self.cords[2])
                top_right[1] = self.cords[1] + a
            else:
                bottom_left[0] = self.cords[0] + a
                bottom_left[1] = min(self.cords[1], self.cords[3])
                bottom_right[0] = max(self.cords[0], self.cords[2])
                bottom_right[1] = min(self.cords[1], self.cords[3])
                top_left[0] = self.cords[0] + a
                top_left[1] = max(self.cords[1], self.cords[3])
                top_right[0] = max(self.cords[0], self.cords[2])
                top_right[1] = max(self.cords[1], self.cords[3])
            points = [x for x in [bottom_left, bottom_right, top_right, top_left] if not x in [self.cords[:2], self.cords[2:]]]
            p = []
            for po in points:
                p += po
            self.result = "{0} {1} {2} {3}".format(*p)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask459ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

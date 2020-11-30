class CodeforcesTask559ASolution:
    def __init__(self):
        self.result = ''
        self.a = []

    def read_input(self):
        self.a = [int(x) for x in input().split(" ")]

    def process_task(self):
        dir_left_left = True
        dir_right_right = True
        last_width = self.a[2]
        height = self.a[0] + self.a[1]
        pos = 0
        triangles = 0
        going_left = self.a[1]
        going_right = self.a[3]
        while pos < height:
            width = last_width
            if dir_left_left and dir_right_right:
                width += 1
            elif not dir_left_left and not dir_right_right:
                width -= 1
            if dir_left_left:
                going_left -= 1
                if not going_left:
                    dir_left_left = False
            if dir_right_right:
                going_right -= 1
                if not going_right:
                    dir_right_right = False
            triangles += last_width + width
            last_width = width
            pos += 1
        self.result = str(triangles)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask559ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

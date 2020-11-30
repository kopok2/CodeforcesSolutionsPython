def is_face(sub_img):
    for c in "face":
        if not c in sub_img:
            return False
    return True


class CodeforcesTask549ASolution:
    def __init__(self):
        self.result = ''
        self.dims = [0, 0]
        self.image = []

    def read_input(self):
        self.dims = [int(x) for x in input().split(" ")]
        for x in range(self.dims[0]):
            self.image.append(input())

    def process_task(self):
        faces = 0
        for x in range(self.dims[1] - 1):
            for y in range(self.dims[0] - 1):
                substr = self.image[y][x:x+2] + self.image[y+1][x:x+2]
                if is_face(substr):
                    faces += 1
        self.result = str(faces)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask549ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

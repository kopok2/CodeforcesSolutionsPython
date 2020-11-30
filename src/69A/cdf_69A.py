class CodeforcesTask69ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.forces = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.forces.append([int(y) for y in input().split(" ")])

    def process_task(self):
        resulting_vector = [0, 0, 0]
        for force in self.forces:
            for dim in range(3):
                resulting_vector[dim] += force[dim]
        if resulting_vector == [0, 0, 0]:
            self.result = "YES"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask69ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

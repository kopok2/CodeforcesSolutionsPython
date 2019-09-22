class CodeforcesTask785ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.polyhedrons = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.polyhedrons.append(input())

    def process_task(self):
        polyhedrons = {
            'Tetrahedron': 4,
            'Cube': 6,
            'Octahedron': 8,
            'Dodecahedron': 12,
            'Icosahedron': 20
        }
        faces = 0
        for p in self.polyhedrons:
            faces += polyhedrons[p]
        self.result = str(faces)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask785ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

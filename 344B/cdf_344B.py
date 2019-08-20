from operator import itemgetter


class CodeforcesTask344BSolution:
    def __init__(self):
        self.result = ''
        self.a_b_c = []

    def read_input(self):
        self.a_b_c = [int(x) for x in input().split(" ")]

    def process_task(self):
        a = self.a_b_c[0]
        b = self.a_b_c[1]
        c = self.a_b_c[2]
        if a > b + c or b > a + c or c > a + b:
            self.result = "Impossible"
        else:
            connections = [0, 0, 0]
            updating = [[0, a], [1, b], [2, c]]
            cannot = False
            while sum(connections) * 2 != sum(self.a_b_c) and not cannot:
                updating.sort(key=itemgetter(1), reverse=True)
                update_rate = updating[1][1] - updating[2][1]
                if not update_rate:
                    if updating[1][1]:
                        update_rate = updating[1][1] // 4
                        if not update_rate:
                            update_rate = 1
                    else:
                        cannot = True
                updating[0][1] -= update_rate
                updating[1][1] -= update_rate
                if updating[0][0] > updating[1][0]:
                    if updating[0][0] - updating[1][0] > 1:
                        connections[2] += update_rate
                    else:
                        connections[updating[1][0]] += update_rate
                else:
                    if updating[1][0] - updating[0][0] > 1:
                        connections[2] += update_rate
                    else:
                        connections[updating[0][0]] += update_rate
            if cannot:
                self.result = "Impossible"
            else:
                self.result = " ".join([str(x) for x in connections])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask344BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

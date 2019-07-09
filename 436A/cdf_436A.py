from operator import itemgetter


def has_to_eat(food_type, height, food):
    result = 0
    for candie in food:
        if candie[0] == food_type or food_type == -1:
            if height >= candie[1]:
                candie[1] = 1000000000000000000
                return candie[0], candie[2]
    return result


class CodeforcesTask436ASolution:
    def __init__(self):
        self.result = ''
        self.n_x = []
        self.candies = []

    def read_input(self):
        self.n_x = [int(x) for x in input().split(" ")]
        for x in range(self.n_x[0]):
            self.candies.append([int(x) for x in input().split(" ")])

    def process_task(self):
        self.candies = sorted(self.candies, key=itemgetter(2), reverse=True)
        #print(self.candies)
        jump = self.n_x[1]
        eat = 1
        candies = [x.copy() for x in self.candies]
        next = has_to_eat(eat, jump, candies)
        eaten = 0
        while next:
            eaten += 1
            jump += next[1]
            if next[0]:
                eat = 0
            else:
                eat = 1
            next = has_to_eat(eat, jump, candies)
        jump = self.n_x[1]
        eat = 0
        candies = [x.copy() for x in self.candies]
        next = has_to_eat(eat, jump, candies)
        eaten1 = 0
        while next:
            eaten1 += 1
            jump += next[1]
            if next[0]:
                eat = 0
            else:
                eat = 1
            next = has_to_eat(eat, jump, candies)
        self.result = str(max(eaten, eaten1))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask436ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

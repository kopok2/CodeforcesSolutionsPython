class CodeforcesTask151BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.friends = []
        self.books = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.friends.append(input().split(" "))
            self.books.append([])
            for y in range(int(self.friends[-1][0])):
                self.books[-1].append([int(x) for x in "".join(input().split("-"))])

    def process_task(self):
        taxiars = []
        pizzaman = []
        cafes = []
        for x in range(self.n):
            for y in range(int(self.friends[x][0])):
                if self.books[x][y].count(self.books[x][y][0]) == 6:
                    taxiars.append(self.friends[x][1])
                elif self.books[x][y] == sorted(self.books[x][y], reverse=True) and sum([self.books[x][y].count(z) ** 2 for z in self.books[x][y]]) == 6:
                    pizzaman.append(self.friends[x][1])
                else:
                    cafes.append(self.friends[x][1])
        names = [x[1] for x in self.friends]
        taxi_chosen = []
        max_taxi = 0
        for taxi in list(set(taxiars)):
            cnt = taxiars.count(taxi)
            max_taxi = max(max_taxi, cnt)
        for taxi in names:
            cnt = taxiars.count(taxi)
            if cnt == max_taxi:
                taxi_chosen.append(taxi)
        pizza_chosen = []
        max_pizza = 0
        for pizza in list(set(pizzaman)):
            cnt = pizzaman.count(pizza)
            max_pizza = max(max_pizza, cnt)
        for pizza in names:
            cnt = pizzaman.count(pizza)
            if cnt == max_pizza:
                pizza_chosen.append(pizza)
        cafe_chosen = []
        max_cafe = 0
        for cafe in list(set(cafes)):
            cnt = cafes.count(cafe)
            max_cafe = max(max_cafe, cnt)
        for cafe in names:
            cnt = cafes.count(cafe)
            if cnt == max_cafe:
                cafe_chosen.append(cafe)
        self.result = "If you want to call a taxi, you should call: {0}.\n".format(", ".join(taxi_chosen))
        self.result += "If you want to order a pizza, you should call: {0}.\n".format(", ".join(pizza_chosen))
        self.result += "If you want to go to a cafe with a wonderful girl, you should call: {0}.".format(", ".join(cafe_chosen))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask151BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

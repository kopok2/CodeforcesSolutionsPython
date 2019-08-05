from operator import itemgetter


class CodeforcesTask294BSolution:
    def __init__(self):
        self.result = ''
        self.books_count = 0
        self.books_dims = []

    def read_input(self):
        self.books_count = int(input())
        for x in range(self.books_count):
            self.books_dims.append([int(y) for y in input().split(" ")])

    def process_task(self):
        v1 = sum([1 for x in self.books_dims if x[0] == 1])
        v2 = sum([1 for x in self.books_dims if x[0] == 2])
        v1_books = [x[1] for x in self.books_dims if x[0] == 1]
        v2_books = [x[1] for x in self.books_dims if x[0] == 2]
        v1_books.sort()
        v2_books.sort()
        minimum = v1 + v2 * 2
        for x in range(v1 + 1):
            for y in range(v2 + 1):
                width = x + y * 2
                thickness = sum(v1_books[:(v1 - x)]) + sum(v2_books[:(v2 - y)])
                if thickness <= width:
                    minimum = min(minimum, width)
        self.result = str(minimum)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask294BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

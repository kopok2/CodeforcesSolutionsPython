class CodeforcesTask245BSolution:
    def __init__(self):
        self.result = ''
        self.adress = ''

    def read_input(self):
        self.adress = input()

    def process_task(self):
        result = ''
        if len(self.adress.split("ftp")[0]):
            result = "http://" + self.adress.split("http", 1)[1]
        else:
            result = "ftp://" + self.adress.split("ftp", 1)[1]
        result = result.replace("//ru", "$$$$").replace("ru", ".ru/", 1).replace("$$$$", "//ru")
        if result[-1] == "/":
            result = result[:-1]
        self.result = result

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask245BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

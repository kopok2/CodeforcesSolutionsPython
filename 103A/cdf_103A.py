class CodeforcesTask103ASolution:
    def __init__(self):
        self.result = ''
        self.quest_num = 0
        self.questions = []

    def read_input(self):
        self.quest_num = int(input())
        self.questions = [int(x) for x in input().split(" ")]

    def process_task(self):
        clicks = 0
        position = 1
        while not position > self.quest_num:
            if self.questions[position - 1] > 1:
                clicks += (self.questions[position - 1] - 1) * position + 1
                position += 1
            else:
                clicks += 1
                position += 1

        self.result = str(clicks)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask103ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

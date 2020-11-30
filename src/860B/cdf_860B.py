class CodeforcesTask860BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.phones = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.phones.append(input())

    def process_task(self):
        phone_book = {}
        for phone in self.phones:
            for x in range(1, len(phone) + 1):
                for y in range(len(phone) - x + 1):
                    subnum = phone[y:y + x]
                    #print(phone, subnum, y, y + x, x)
                    if subnum in phone_book.keys():
                        if phone_book[subnum] != phone:
                            phone_book[subnum] = False
                    else:
                        phone_book[subnum] = phone
        results = []
        for phone in self.phones:
            found = False
            for x in range(1, len(phone) + 1):
                for y in range(len(phone) - x + 1):
                    subnum = phone[y:y + x]
                    if subnum in phone_book.keys():
                        if phone_book[subnum]:
                            found = True
                            results.append(subnum)
                            break
                if found:
                    break
        self.result = "\n".join([str(x) for x in results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask860BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

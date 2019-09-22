class CodeforcesTask87BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.expressions = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.expressions.append(input().split(" "))

    def process_task(self):
        result = []
        lang_dict = {"void":0}
        for expr in self.expressions:
            if expr[0] == "typedef":
                up = expr[1].count("*")
                down = expr[1].count("&")
                nm = expr[1].replace("*", "").replace("&", "")
                if nm in lang_dict:
                    if lang_dict[nm] == -1:
                        lang_dict[expr[2]] = -1
                    else:
                        lang_dict[expr[2]] = max(-1, lang_dict[nm] + up - down)
                else:
                    lang_dict[expr[2]] = -1
            elif expr[0] == "typeof":
                up = expr[1].count("*")
                down = expr[1].count("&")
                nm = expr[1].replace("*", "").replace("&", "")
                if nm in lang_dict:
                    balance = max(lang_dict[nm] + up - down, -1)
                    if balance == -1 or lang_dict[nm] == -1:
                        result.append("errtype")
                    else:
                        result.append("void" + "*" * balance)
                else:
                    result.append("errtype")
        self.result = "\n".join(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask87BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

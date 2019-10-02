import os
import requests
from pyquery import PyQuery
import webbrowser
from random import randrange

TEST_TEMPLATE_PATH = "empty_test.py"
TESTCASE_TEMPLATE_PATH = "empty_testcase.py"
SOLUTION_TEMPLATE_PATH = "empty_solution.py"
LEVEL = "B"
RANDOMIZED = True


def get_task():
    NUMBER = randrange(1150) if RANDOMIZED else int(input("Enter problem number:"))
    TASK_ID = str(NUMBER) + LEVEL
    while TASK_ID in os.listdir():
        NUMBER = randrange(1150)
        TASK_ID = str(NUMBER) + LEVEL

    url = "http://codeforces.com/problemset/problem/{0}/{1}".format(NUMBER, LEVEL)
    r = requests.get(url)
    pq = PyQuery(r.text)
    title = pq('div.title').eq(0)
    print("Task no. {0}".format(TASK_ID))
    print(title.text())

    print("Generating files...")
    os.mkdir(TASK_ID)
    open("{0}/cdf_{0}.py".format(TASK_ID), "w").write(open(SOLUTION_TEMPLATE_PATH, "r").read().format(TASK_ID))

    print("Generating tests...")
    TESTS = ""
    INPUTS = [test("pre").text() for test in pq.items(".input")]
    RESULTS = [test("pre").text() for test in pq.items(".output")]
    i = 1
    for In_val, Out_val in zip(INPUTS, RESULTS):
        TESTS += open(TESTCASE_TEMPLATE_PATH, "r").read().format(TASK_ID, i, str(In_val.split("\n")), Out_val.replace("\n", "{0}"))
        i += 1
    open("{0}/test_cdf_{0}.py".format(TASK_ID), "w").write(open(TEST_TEMPLATE_PATH, "r").read().format(TASK_ID, TESTS.format("\\n")))

    print("Initialization successful.")
    webbrowser.open(url)


if __name__ == "__main__":
    get_task()

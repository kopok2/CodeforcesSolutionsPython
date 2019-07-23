from fractions import Fraction


class CodeforcesTask569ASolution:
    def __init__(self):
        self.result = ''
        self.t_s_q = []

    def read_input(self):
        self.t_s_q = [int(x) for x in input().split(" ")]

    def process_task(self):
        starts = 1
        downloaded = Fraction(self.t_s_q[1])
        speed = Fraction(self.t_s_q[2] - 1) / Fraction(self.t_s_q[2])
        duration = Fraction(self.t_s_q[0])
        playback = Fraction()
        step = Fraction(0.5)
        while playback < duration:
            playback += step
            downloaded += speed * step
            if playback >= duration:
                break
            if playback >= downloaded:
                starts += 1
                playback = 0
            #print(downloaded, playback)
        self.result = str(starts)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask569ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

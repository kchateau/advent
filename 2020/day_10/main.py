import itertools
import numpy as np
from more_itertools import run_length

class AdapterArray():
    def parse_input(self, filename):
        with open(filename, "r") as my_file:
            data = []
            for line in my_file:
               data.append(int(line.strip('\n')))

        return data

    def count_joltage_diff(self, adapter_list):
        num_diff_ones = 1
        num_diff_threes = 1
        for index in range(0, len(adapter_list) - 1):
            if (adapter_list[index] + 1) == adapter_list[index + 1]:
                num_diff_ones += 1
            if (adapter_list[index] + 3) == adapter_list[index + 1]:
                num_diff_threes += 1

        return str(num_diff_ones * num_diff_threes)

    # def question_2(self, curr_adapter, adapter_list):
    #     # print(curr_adapter)
    #     global total_arrangements
    #     if curr_adapter == 164:
    #         # print(total_arrangements)
    #         total_arrangements += 1
    #         return
    #     if (curr_adapter + 1) in adapter_list:
    #         self.question_2(curr_adapter + 1, adapter_list)
    #     if (curr_adapter + 2) in adapter_list:
    #         self.question_2(curr_adapter + 2, adapter_list)
    #     if (curr_adapter + 3) in adapter_list:
    #         self.question_2(curr_adapter + 3, adapter_list)

    def question_2(self):
        with open("input.txt") as f:
            numbers = sorted([int(x) for x in f])

        cands = [e for i, e in run_length.encode(np.diff([0]+numbers)) if i == 1 and e > 1]
        combinations = {2: 2, 3: 4, 4: 7}
        return str(np.prod([combinations[e] for e in cands]))

    def main(self):
        global total_arrangements
        adapter_list = self.parse_input("input.txt")
        adapter_list.sort()
        total_arrangements = 0
        print("Question 1: " + self.count_joltage_diff(adapter_list))
        print("Question 2: " + self.question_2())

if __name__ == "__main__":
    AdapterArray().main()
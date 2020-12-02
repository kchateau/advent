from itertools import combinations 
import functools
from functools import partial

class ReportRepair():    
    def parse_input(filename):
        with open(filename, "r") as my_file:
            input_parsed = []
            for line in my_file:
                input_parsed.append(int(line))

            return input_parsed

    def solve(func, val, numbers, target_num):
        num_list = list(filter(partial(func, target_num=target_num), list(combinations(numbers, val))))

        return functools.reduce(lambda x, y: x * y, num_list[0])

    def doubles(val, target_num): 
        return sum(val) == target_num

    def triples(val, target_num): 
        return sum(val) == target_num

    numbers = parse_input("input.txt")
    target_num = 2020

    print("Doubles: " + str(solve(doubles, 2, numbers, target_num)))
    print("Triples: " + str(solve(triples, 3, numbers, target_num)))
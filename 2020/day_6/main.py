from collections import Counter

class CustomCustoms():
    def parse_intput(filename):
        with open(filename, "r") as my_file:
            my_file_split = my_file.read().split("\n\n")
            return my_file_split

    def question_1(data):
        total_yes = 0
        for string in data:
            x = string.replace("\n", "") 
            y = "".join(set(x))
            total_yes += len(y)

        return total_yes

    def question_2(data):
            total_yes = 0
            for string in data:
                num_passengers = string.count("\n") + 1
                x = string.replace("\n", "") 
                all_freq = {} 
                for i in x: 
                    if i in all_freq: 
                        all_freq[i] += 1
                    else: 
                        all_freq[i] = 1
                for (key, val) in all_freq.items():
                    if val >= num_passengers:
                        total_yes += 1

            return total_yes

    data = parse_intput("input.txt")

    print("Question 1: " + str(question_1(data)))
    print("Question 1: " + str(question_2(data)))
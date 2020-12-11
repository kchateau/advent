class EncodingError():
    def parse_input(self, filename):
        with open(filename, "r") as my_file:
            data = []
            for line in my_file:
               data.append(int(line.strip('\n')))

        return data

    def check_list_for_pair(self, my_list, goal):
        for x in my_list:
            for y in my_list[1:]:
                if ((x + y) == goal) and x != y:
                    return True
        return False

    def check_list_for_running_total(self, list_data):
        ans = 0
        goal = 26796446
        running_total = 0
        running_total_list = []
        for value in list_data:
            running_total += value
            running_total_list.append(value)
            if running_total == goal:
                running_total_list.sort()
                ans = running_total_list[0] + running_total_list[-1]
                print("Question 2: " + str(ans))
                return True
            if running_total > goal:
                return False

    def question_1(self, my_list, goal):
        if self.check_list_for_pair(my_list[0:25], goal) == True:
            my_list.pop(0)
            goal = my_list[25]
            self.question_1(my_list, goal)
        else:
            print("Quesion 1: " + str(goal))
            return
    
    def question_2(self, question_2_data):
        if self.check_list_for_running_total(question_2_data) is False:
            question_2_data.pop(0)
            self.question_2(question_2_data)

    def main(self):
        question_1_data = self.parse_input("input.txt")
        question_2_data = self.parse_input("input.txt")
        goal = question_1_data[25]
        self.question_1(question_1_data, goal)
        self.question_2(question_2_data)

if __name__ == "__main__":
    EncodingError().main()
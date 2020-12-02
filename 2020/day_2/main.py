class ReportRepair():    
    def parse_input(filename):
        with open(filename, "r") as my_file:
            input_parsed = []
            for line in my_file:
                line = line.split()
                input_parsed.append({
                    "min": int(line[0].split("-")[0]),
                    "max": int(line[0].split("-")[1]),
                    "char": line[1][:-1],
                    "str": line[2]
                })

            return input_parsed

    def question_1(password_dict):
        num_valid_password = 0
        for corrupted_password in password_dict:
            if(corrupted_password['str'].count(corrupted_password['char']) >= corrupted_password['min'] and
                corrupted_password['str'].count(corrupted_password['char']) <= corrupted_password['max']):
                    num_valid_password += 1

        print("Question 1: " + str(num_valid_password) + " valid passwords.")

    def question_2(password_dict):
        num_valid_password = 0
        for corrupted_password in password_dict:
            i = 0
            if(corrupted_password['str'][corrupted_password['min']-1] is corrupted_password['char']):
                i += 1
            if(corrupted_password['str'][corrupted_password['max']-1] is corrupted_password['char']):
                i += 1
                    
            if i is 1:
                num_valid_password += 1

        print("Question 2: " + str(num_valid_password) + " valid passwords.")

    password_dict = parse_input("input.txt")
    question_1(password_dict)
    question_2(password_dict)
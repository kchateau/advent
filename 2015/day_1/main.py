class NotQuiteLisp():
    def parse_input(filename):
        with open(filename, "r") as my_file:
            floor = 0
            floor_pos = 0
            for line in my_file:
                for char in line:
                    floor_pos += 1
                    if char == "(":
                        floor += 1

                    if char == ")":
                        floor -= 1
                        if floor is -1:
                            print("Hit basement at " + str(floor_pos))


            return floor

    print("Question 1: " + str(parse_input("input.txt")))
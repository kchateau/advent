class TobogganTrajectory():
    def parse_input(filename):
        with open(filename, "r") as my_file:
            input_parsed = []
            for line in my_file:
                input_parsed.append(list(line[:-1]))
            
            return input_parsed

    def traverse_slope(slope_map, right_inc, down_inc):
        tree_count = 0
        slope_length = len(slope_map[0])
        x_coord = 0
        for slope_section in slope_map[::down_inc]:
            if(slope_section[x_coord] is "#"):
                tree_count += 1
            x_coord += right_inc
            if(x_coord > 30):
                x_coord = x_coord - 31

        return tree_count

    slope_map = parse_input("input.txt")

    question_1_total = traverse_slope(slope_map, 3, 1)
    question_2_total = (traverse_slope(slope_map, 1, 1) *
        traverse_slope(slope_map, 3, 1) *
        traverse_slope(slope_map, 5, 1) *
        traverse_slope(slope_map, 7, 1) *
        traverse_slope(slope_map, 1, 2))

    print("Question 1: " + str(question_1_total))
    print("Question 2: " + str(question_2_total))
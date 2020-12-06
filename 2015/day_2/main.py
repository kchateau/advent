class OrderWrapping():
    def parse_input(filename):
        total_sq_footage = 0
        ribbon_needed = 0
        with open(filename, "r") as my_file:
            for gift in my_file:
                gift_dimensions = gift.strip('\n').split('x')
                gift_dimensions_int = []
                for dimension in gift_dimensions:
                    gift_dimensions_int.append(int(dimension))
                gift_dimensions_int.sort()
                ribbon_needed += gift_dimensions_int[0] * gift_dimensions_int[1] * gift_dimensions_int[2]
                ribbon_needed += gift_dimensions_int[0] + gift_dimensions_int[0] + gift_dimensions_int[1] + gift_dimensions_int[1]
                side_1 = gift_dimensions_int[0] * gift_dimensions_int[1]
                side_2 = gift_dimensions_int[0] * gift_dimensions_int[2]
                side_3 = gift_dimensions_int[1] * gift_dimensions_int[2]

                total_sq_footage += ((2 * side_1) + (2 * side_2) + (2 * side_3) + int(min(side_1, side_2, side_3)))
   
        print("Question 1: " + str(total_sq_footage))
        print("Question 2: " + str(ribbon_needed))

    parse_input("input.txt")
class ReportRepair():
        
    def parse_input(filename):
        with open(filename, "r") as my_file:
            input_parsed = []
            for line in my_file:
                input_parsed.append(int(line))

            return input_parsed

    # Given a list of ints and a target value, return the multiplication of 2 numbers in the list that add to the target
    def doubles(numbers, target_number):
        for i, number in enumerate(numbers[:-1]):
            complementary = target_number - number
            if complementary in numbers[i+1:]:
                return(number * complementary)

    numbers = parse_input("input.txt")
    target_number = 2020

    ans = doubles(numbers, target_number)
    print(ans)

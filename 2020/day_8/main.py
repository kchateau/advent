class HandHeldHalting():
    def parse_input(self, filename):
        with open(filename, "r") as my_file:
            instructions = []
            for line in my_file:
                instructions.append(line.strip('\n').split(' '))

        return instructions

    def question_1(self, instructions):
        acc = 0
        i = 0
        while True:
            if instructions[i] == "hit":
                break
            math = instructions[i][1][0]
            amount = instructions[i][1][1:]
            instruction = instructions[i][0]
            if instruction == "acc":
                if math == '+':
                    acc += int(amount)
                else:
                    acc -= int(amount)
            if instruction == "jmp":
                if math == "+":
                    instructions[i] = "hit"
                    i += int(amount)
                    continue
                if math == "-":
                    instructions[i] = "hit"
                    i -= int(amount)
                    continue

            if instructions[i] == 'hit':
                return "probably infinite"
            instructions[i] = "hit"
            i += 1
        return acc

    def is_infinite(self, instructions):
        acc = 0
        i = 0
        while True:
            if i >= len(instructions):
                return acc
            if instructions[i] == "hit":
                return "infinite loop"
            
            math = instructions[i][1][0]
            amount = instructions[i][1][1:]
            instruction = instructions[i][0]
            if instruction == "acc":
                if math == '+':
                    acc += int(amount)
                else:
                    acc -= int(amount)
            if instruction == "jmp":
                if math == "+":
                    instructions[i] = "hit"
                    i += int(amount)
                    continue
                if math == "-":
                    instructions[i] = "hit"
                    i -= int(amount)
                    continue

            if instructions[i] == 'hit':
                return "probably infinite"
            instructions[i] = "hit"
            i += 1
        # return acc

    def main(self):
        acc = 0
        instructions = self.parse_input('input.txt')
        instructions_2 = self.parse_input('input.txt')
        ans_1 = self.question_1(instructions)
        print("Question 1: " + str(ans_1))

        for (index, instruction) in enumerate(instructions_2):
            # i hate python indenting

        #    if instruction[0] == 'nop':
        #        instructions_copy = self.parse_input('input.txt')
        #        instructions_copy[index][0] = 'jmp'
        #        ans = self.is_infinite(instructions_copy)
        #        if ans != 'infinite loop':
        #            print(ans)

            if instruction[0] == 'jmp':
                instructions_copy = self.parse_input('input.txt')
                instructions_copy[index][0] = 'nop'
                ans = self.is_infinite(instructions_copy)
                if ans != 'infinite loop':
                    print(ans)

if __name__ == "__main__":
    HandHeldHalting().main()
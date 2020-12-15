from pprint import pprint

class SeatingSystem():
    def parse_input(self, filename):
        with open(filename, "r") as my_file:
            seat_row_list = []
            for line in my_file:
               seat_row_list.append(list(line.strip('\n')))

        return seat_row_list

    def iterate_seats(self, seat_row_list, new_seat_row_list):
        for (row_index, seat_row) in enumerate(seat_row_list):
            for (seat_index, seat) in enumerate(seat_row):
                if seat is "L":
                    adjacent_seats = self.get_adjacent(seat_row_list, row_index, seat_index, seat_row)
                    if '#' not in adjacent_seats:
                        new_seat_row_list[row_index][seat_index] = '#'
                    else:
                        new_seat_row_list[row_index][seat_index] = 'L'

                if seat is '#':
                    adjacent_seats = self.get_adjacent(seat_row_list, row_index, seat_index, seat_row)
                    count_occupied = ''.join(adjacent_seats).count('#')
                    if count_occupied >= 4:
                        new_seat_row_list[row_index][seat_index] = 'L'
                    else:
                        new_seat_row_list[row_index][seat_index] = '#'

    def iterate_seats_2(self, seat_row_list, new_seat_row_list):
        for (row_index, seat_row) in enumerate(seat_row_list):
            for (seat_index, seat) in enumerate(seat_row):
                if seat is "L":
                    adjacent_seats = []
                    adjacent_seats.append(self.get_up(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_down(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_left(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_right(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_up_left(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_up_right(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_down_left(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_down_right(seat_row_list, row_index, seat_index, seat_row))
                    if '#' not in adjacent_seats:
                        new_seat_row_list[row_index][seat_index] = '#'
                    else:
                        new_seat_row_list[row_index][seat_index] = 'L'

                if seat is '#':
                    adjacent_seats = []
                    adjacent_seats.append(self.get_up(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_down(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_left(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_right(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_up_left(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_up_right(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_down_left(seat_row_list, row_index, seat_index, seat_row))
                    adjacent_seats.append(self.get_down_right(seat_row_list, row_index, seat_index, seat_row))
                    count_occupied = ''.join(adjacent_seats).count('#')
                    if count_occupied >= 5:
                        new_seat_row_list[row_index][seat_index] = 'L'
                    else:
                        new_seat_row_list[row_index][seat_index] = '#'

    def get_up(self, seat_row_list, row_index, seat_index, seat_row):
        while row_index is not 0: # Up
            if seat_row_list[row_index - 1][seat_index] is not '':
                return seat_row_list[row_index - 1][seat_index]
            else:
                row_index -= 1

        return ''

    def get_down(self, seat_row_list, row_index, seat_index, seat_row):
        while row_index is not len(seat_row_list) - 1: # Down
            if seat_row_list[row_index + 1][seat_index] is not '':
                return seat_row_list[row_index + 1][seat_index]
            else:
                row_index += 1

        return ''

    def get_right(self, seat_row_list, row_index, seat_index, seat_row):
        while seat_index < len(seat_row) - 1: # Right
            if seat_row_list[row_index][seat_index + 1] is not '':
                return seat_row_list[row_index][seat_index + 1]
            else:
                seat_index += 1

        return ''
    
    def get_left(self, seat_row_list, row_index, seat_index, seat_row):
        while seat_index > 0: # Left
            if seat_row_list[row_index][seat_index - 1] is not '':
                return seat_row_list[row_index][seat_index - 1]
            else:
                seat_index -= 1

        return ''

    def get_up_left(self, seat_row_list, row_index, seat_index, seat_row):
        while row_index is not 0 and seat_index > 0: # Up Left
            if seat_row_list[row_index - 1][seat_index - 1] is not '':
                return seat_row_list[row_index - 1][seat_index - 1]
            else:
                row_index -= 1
                seat_index -= 1

        return ''
    
    def get_up_right(self, seat_row_list, row_index, seat_index, seat_row):
        while row_index is not 0 and seat_index < len(seat_row) - 1: #Up Right
            if seat_row_list[row_index - 1][seat_index + 1] is not '':
                return seat_row_list[row_index - 1][seat_index + 1]
            else:
                row_index -= 1
                seat_index += 1

        return ''

    def get_down_left(self, seat_row_list, row_index, seat_index, seat_row):
        while row_index is not len(seat_row_list) - 1 and seat_index > 0: # Down Left
            if seat_row_list[row_index + 1][seat_index - 1] is not '':
                return seat_row_list[row_index + 1][seat_index - 1]
            else:
                row_index += 1
                seat_index -= 1

        return ''

    def get_down_right(self, seat_row_list, row_index, seat_index, seat_row):
        while row_index is not len(seat_row_list) - 1 and seat_index < len(seat_row) - 1: # Down Right
            if seat_row_list[row_index + 1][seat_index + 1] is not '':
                return seat_row_list[row_index + 1][seat_index + 1]
            else:
                row_index += 1
                seat_index += 1

        return ''

    def get_adjacent(self, seat_row_list, row_index, seat_index, seat_row):
        adjacent_seats = []
        if row_index is not 0: # Up
            adjacent_seats.append(seat_row_list[row_index - 1][seat_index])
        if row_index is not len(seat_row_list) - 1: # Down
            adjacent_seats.append(seat_row_list[row_index + 1][seat_index])
        if seat_index > 0: # Left
            adjacent_seats.append(seat_row_list[row_index][seat_index - 1])
        if seat_index < len(seat_row) - 1: # Right
            adjacent_seats.append(seat_row_list[row_index][seat_index + 1])
        if row_index is not 0 and seat_index > 0: # Up Left
            adjacent_seats.append(seat_row_list[row_index - 1][seat_index - 1])
        if row_index is not 0 and seat_index < len(seat_row) - 1: # Up Right
            adjacent_seats.append(seat_row_list[row_index - 1][seat_index + 1])
        if row_index is not len(seat_row_list) - 1 and seat_index > 0: # Down Left
            adjacent_seats.append(seat_row_list[row_index + 1][seat_index - 1])
        if row_index is not len(seat_row_list) - 1 and seat_index < len(seat_row) - 1: # Down Right
            adjacent_seats.append(seat_row_list[row_index + 1][seat_index + 1])

        return adjacent_seats

    def create_empty_list_copy(self, list_to_copy):
        new_list = []
        for row in list_to_copy:
            row_list = []
            for character in row:
                row_list.append('')
            new_list.append(row_list)
        return new_list
    
    def question_1(self, seat_list):
        while True:
            empty_list = self.create_empty_list_copy(seat_list)
            self.iterate_seats(seat_list, empty_list)
            if seat_list == empty_list:
                count = 0
                for seat_row in seat_list:
                    for seat in seat_row:
                        if seat is '#':
                            count += 1
                print("Question 1: " + str(count))
                break
            seat_list = empty_list
        return

    def question_2(self, seat_list):
        while True:
            empty_list = self.create_empty_list_copy(seat_list)
            self.iterate_seats_2(seat_list, empty_list)
            if seat_list == empty_list:
                count = 0
                for seat_row in seat_list:
                    for seat in seat_row:
                        if seat is '#':
                            count += 1
                print("Question 2: " + str(count))
                break
            seat_list = empty_list
        return

    def main(self):
        seat_row_list = self.parse_input("input.txt")

        self.question_1(seat_row_list)
        self.question_2(seat_row_list)

if __name__ == "__main__":
    SeatingSystem().main()
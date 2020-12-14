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


    def get_adjacent(self, seat_row_list, row_index, seat_index ,seat_row):
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



    def main(self):
        seat_row_list = self.parse_input("input.txt")
        seat_row_list_copy = self.parse_input("input.txt")
        while True:
            empty_list = self.create_empty_list_copy(seat_row_list)
            self.iterate_seats(seat_row_list, empty_list)
            if seat_row_list == empty_list:
                count = 0
                for seat_row in seat_row_list:
                    for seat in seat_row:
                        if seat is '#':
                            count += 1
                print(count)
                break
            seat_row_list = empty_list

if __name__ == "__main__":
    SeatingSystem().main()
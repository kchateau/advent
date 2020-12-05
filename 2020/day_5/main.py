import math

class BinaryBoarding():
    def parse_input(self, filename):
        with open(filename, "r") as my_file:
            seats = []
            for line in my_file:
                seats.append(line.strip())
                
            return seats

    def split_row(self, min, max, seat):
        diff = (math.floor((max - min)/2) + 1)
       
        if len(seat) is 0:
            return max
        if seat[0] == "F":
            return self.split_row(min, max - diff, seat[1:])
        if seat[0] == "B":
            return self.split_row(min + diff, max, seat[1:])

    def split_column(self, min, max, seat):
        diff = (math.floor((max - min)/2) + 1)

        if len(seat) is 0:
            return min
        if seat[0] == "L":
            return self.split_column(min, max - diff, seat[1:])
        if seat[0] == "R":
            return self.split_column(min + diff, max, seat[1:])

    def main(self):
        ans = 0
        seat_id_list = []
        min_row = 0
        max_row = 127
        min_col = 0
        max_col = 7

        seat_list = self.parse_input("input.txt")

        for seat in seat_list:
            row_val = self.split_row(min_row, max_row, seat[:-3])
            col_val = self.split_column(min_col, max_col, seat[7:])

            val = (row_val * 8) + col_val

            seat_id_list.append(val)

            if val > ans:
                ans = val 

        print("Question 1: " + str(ans))
        seat_id_list.sort()

        for i, x in enumerate(seat_id_list):
            y = seat_id_list[i+1]
            if (y - x) is not 1:
                print("Question 2: " + str(x + 1))
                return

if __name__ == "__main__":
    BinaryBoarding().main()
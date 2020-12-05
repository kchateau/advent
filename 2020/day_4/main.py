import re

class PassportProcessing():
    valid_passport_count = 0

    def parse_input(self, filename):
        with open(filename, "r") as my_file:
            lines = my_file.read()
            input_parsed = lines.split('\n\n')
            passport_data = []
            for passport in input_parsed:
                passport_data.append(passport.split())
                
            return passport_data

    def create_passport_dict(self, passport):
        passport_dict = {}
        for passport_data in passport:
            x,y = passport_data.split(':')
            passport_dict[x] = y
        return passport_dict
            
    def byr_is_valid(self, byr):
        return (int(byr) >= 1920 and int(byr) <= 2002)

    def iyr_is_valid(self, iyr):
        return (int(iyr) >= 2010 and int(iyr) <= 2020)

    def eyr_is_valid(self, eyr):
        return (int(eyr) >= 2020 and int(eyr) <= 2030)

    def hgt_is_valid(self, hgt):
        height_int = hgt[:-2]
        height_type = hgt[-2:]

        return (height_type == "cm" 
        and int(height_int) >= 150 
        and int(height_int) <= 193) 
        or (height_type == "in" 
        and int(height_int) >= 59 
        and int(height_int) <= 76)

    def hcl_is_valid(self, hcl):
        hcl_nums = hcl[1:]
        regex = re.compile("^[0-9a-fA-F]{6}$")

        return (hcl[0] == "#" and not regex.match(hcl_nums) == None)

    def ecl_is_valid(self, ecl):
        valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return (ecl in valid)

    def pid_is_valid(self, pid):
        regex = re.compile("^\\d{9}$")
        return (not regex.match(pid) == None)

    def passport_is_valid(self, passport):
        return (self.byr_is_valid(passport['byr']) 
            and self.iyr_is_valid(passport['iyr'])
            and self.eyr_is_valid(passport['eyr'])
            and self.hgt_is_valid(passport['hgt'])
            and self.hcl_is_valid(passport['hcl'])
            and self.ecl_is_valid(passport['ecl'])
            and self.pid_is_valid(passport['pid'])
            )

    def passport_validate(self, passport_dict, required_fields):
        if all(requirement in passport_dict for requirement in required_fields):
            if self.passport_is_valid(passport_dict):
                self.valid_passport_count += 1
                print(passport_dict)
            

    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
   
    def main(self):
        data = self.parse_input('input.txt')
        for passport in data:
            passport_dict = self.create_passport_dict(passport)
            self.passport_validate(passport_dict, self.required_fields)

        print(self.valid_passport_count)

if __name__ == "__main__":
    PassportProcessing().main()
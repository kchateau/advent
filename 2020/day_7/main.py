class HandyHaversacks():
    def parse_intput(self, filename):
        with open(filename, "r") as my_file:
            bag_list = []
            for line in my_file:
                bag_list.append(line.strip('\n'))

            return bag_list
                
    def can_hold_gold(self, bag, sub_str):
        return (sub_str in bag)

    def get_unique_list(self, my_list):
        unique_list = []
        for list_item in my_list:
            if list_item not in unique_list:
                unique_list.append(list_item)

        return unique_list

    def question_1(self, bag_types, bags, total):
        before_list = self.get_unique_list(bag_types)
        for bag in bags:
            bag_name = bag.split(' ')[0] + ' ' + bag.split(' ')[1]
            for bag_type in bag_types:
                if(self.can_hold_gold(bag, bag_type)):
                    if(str(bag_name) != str(bag_type)):
                        total += 1  
                        bag_types.append(bag_name)

        after_list = self.get_unique_list(bag_types)

        if len(before_list) is len(after_list):
            print("Question 1: " + str(len(before_list)))
            return
        else:
            self.question_1(bag_types, bags, total)

    def parse_input_2(self, bag_types, bags, total):
        extra_words = ["contain", "no", "other", "bags", "bags.", "bags,", 'bag,', 'bag.']
        split_bags = []
        list_parsed_bags = []
        for bag in bags:
            bag_list = bag.split(' ')
            for word in extra_words:
                while word in bag_list:
                    bag_list.remove(word)

            list_parsed_bags.append(bag_list)

        return list_parsed_bags

    def sort_bags(self, input):
        bag_list = []
        for val in input:
            bag_name = val[0] + ' ' + val[1]
            bag_contained = []
            for x in val:
                bag_contained.append(x)

            bag_list.append(bag_contained)

        return bag_list

    def find_bag_from_contained_bag(self, bags, contained_bag):
        for bag in bags:
            if bag.name == contained_bag.name:
                return(bag)

    def answer_question_2(self, my_bags):
        curr_bag = self.find_bag_from_contained_bag(my_bags, ContainedBag("shiny gold", 1))
        queue = [curr_bag]
        count = 0

        while queue != []:
            count += 1
            curr_bag = queue.pop(0)
            for bag in curr_bag.bags:
                x = self.find_bag_from_contained_bag(my_bags, bag)
                for y in range(int(bag.count)):
                    queue.append(x)

        print("Question 2: " + str(count))

    def main(self):
        my_bags = []
        bag_types = ['shiny gold']
        bags = self.parse_intput("input.txt")
        total = 0
        self.question_1(bag_types, bags, total)
        question_2_parsed_input = self.parse_input_2(bag_types, bags, total)
        # print(question_2_parsed_input)
        sorted_bags = self.sort_bags(question_2_parsed_input)

        for bag in sorted_bags:
            bag_name = bag[0] + ' ' + bag[1]
            contained_bag_list = []

            num_bags = len(bag[2:]) / 3
            bag_without_name = bag[2:]
            for x in range(num_bags):
                # print(x)
                # print(bag_without_name)
                count = bag_without_name.pop(0)
                name = bag_without_name.pop(0) + ' ' + bag_without_name.pop(0)
                contained_bag = ContainedBag(name, count)
                contained_bag_list.append(contained_bag)
                # print(repr(contained_bag))
            my_bag = Bag(bag_name, contained_bag_list)
            my_bags.append(my_bag)

        self.answer_question_2(my_bags)

        

class Bag():
    def __init__(self, name, bags):
        self.name = name
        self.bags = bags

    def __repr__(self):
        return "<Bag name:%s bags:%s>" % (self.name, self.bags)
       

class ContainedBag():
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __repr__(self):
        return "<Contained bag name:%s count:%s>" % (self.name, self.count)
        

if __name__ == "__main__":
    HandyHaversacks().main()
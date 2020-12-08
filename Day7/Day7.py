import re


def check_bags(list_of_bags, picked_colour):
    counter = 0
    list_of_allowed_bags, new_bags = [], [picked_colour]
    while counter < len(list_of_bags):
        for new_bag in new_bags:
            for bag in list_of_bags:
                if new_bag in bag[1:] and bag[0] not in list_of_allowed_bags:
                    list_of_allowed_bags.append(bag[0])
                    new_bags.append(bag[0])
            # new_bags = []
        counter += 1
    print(list_of_allowed_bags)
    print(len(list_of_allowed_bags))


def check_bags_2(list_of_bags, picked_colour):
    number_of_bags = 0
    for bags in list_of_bags:
        if bags[0] == picked_colour:
            for i in range(2, len(bags), 2):
                number_of_bags += bags[i-1] * check_bags_2(list_of_bags, bags[i])
            if bags[1] == 'no other':
                number_of_bags = 1
    return number_of_bags


def parse_line(line):
    bags = []
    for bag in line:
        bag_desc = bag.replace(' bag', '').strip()
        if bag_desc.split(' ')[:1][0].isdigit():
            bags.append(int(bag_desc.split(' ')[:1][0]))
            bags.append(bag_desc[2:])
        else:
            bags.append(bag_desc)
    return bags


def main():
    filename = 'testfile'
    colour = 'shiny gold'
    bags = []
    with open(filename, 'r') as fh:
        for line in fh.readlines():
            bags.append(parse_line(re.findall('\d?\s?\w+\s\w+\sbag', line)))
    """
    Part 1
    """
    # check_bags(bags, colour)
    """
    Part 2
    """
    print(check_bags_2(bags, colour))


if __name__ == '__main__':
    main()
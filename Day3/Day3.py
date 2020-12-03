import math


def read_file_in_array(filename):
    with open(filename, 'r') as fh:
        return fh.readlines()


def go_dow_the_slope(trees):
    x_coordinate = 0
    nbr_of_trees = 0
    for line in trees:
        line = math.ceil(x_coordinate/len(line)+1)*line.strip()
        if line[x_coordinate] == '#':
            nbr_of_trees += 1
        x_coordinate += 3
    print(nbr_of_trees)


def go_down_the_slope_2(trees, increments):
    x_increment, y_increment = increments
    nbr_of_trees, x, y = 0, 0, 0
    while y < len(trees):
        line = trees[y].strip()
        x_modif = x - math.floor(x / len(line)) * len(line)
        if line[x_modif] == '#':
            nbr_of_trees += 1
        x += x_increment
        y += y_increment
    return nbr_of_trees


def main():
    filename = 'inputfile'
    """
    Part 1
    For this the x_coordinate increment was hardcoded in go_down_the_slope.
    """
    # go_dow_the_slope(read_file_in_array(filename))
    """Part 2"""
    list_of_increments = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total_nbr_trees = 1
    for increments in list_of_increments:
        total_nbr_trees *= go_down_the_slope_2(read_file_in_array(filename), increments)
    print(total_nbr_trees)


if __name__ == '__main__':
    main()
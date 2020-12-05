import math


def split_in_halve(directions, limits):
    for direction in directions:
        half = (limits[1] - limits[0])/2
        if direction in ['F', 'L']:
            if limits[1] - limits[0] <= 1:
                return limits[0]
            limits[1] = limits[1] - math.ceil(half)
        elif direction in ['B', 'R']:
            if limits[1] - limits[0] <= 1:
                return limits[1]
            limits[0] = limits[0] + math.ceil(half)
    return limits


def parse_input(directions):
    front_back = ['F', 'B']
    left_right = ['L', 'R']
    if directions[:1] in front_back:
        limits = [0, 127]
        return split_in_halve(directions, limits)
    elif directions[-1:] in left_right:
        limits = [0, 7]
        return split_in_halve(directions, limits)
    else:
        print("Foreign command")


def read_input(filename):
    max_seat_id = 0
    with open(filename, 'r') as fh:
        for line in fh.readlines():
            seat_id = parse_input(line.strip()[:7]) * 8 + parse_input(line.strip()[-3:])
            if seat_id > max_seat_id:
                max_seat_id = seat_id
    return max_seat_id


def main():
    filename = 'inputfile'
    print(read_input(filename))


if __name__ == '__main__':
    main()
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


def day1_function(file_handler):
    max_seat_id = 0
    for line in file_handler:
        seat_id = parse_input(line.strip()[:7]) * 8 + parse_input(line.strip()[-3:])
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id


def day2_function(file_handler):
    seat_ids = []
    for line in file_handler:
        seat_ids.append(parse_input(line.strip()[:7]) * 8 + parse_input(line.strip()[-3:]))
    seat_ids.sort()
    for index, seat_id in enumerate(seat_ids):
        if seat_id != seat_ids[index+1] - 1:
            return seat_id + 1


def read_input(filename):
    with open(filename, 'r') as fh:
        # return day1_function(fh)
        return day2_function(fh)


def main():
    filename = 'inputfile'
    print(read_input(filename))


if __name__ == '__main__':
    main()
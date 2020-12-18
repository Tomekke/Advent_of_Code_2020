
def N(distance):
    print('going north ' + str(distance))
    global waypoint
    waypoint[1] += int(distance)


def S(distance):
    print('going south ' + str(distance))
    global waypoint
    waypoint[1] -= int(distance)


def E(distance):
    print('going east ' + str(distance))
    global waypoint
    waypoint[1] -= int(distance)


def W(distance):
    print('going west ' + str(distance))
    global waypoint
    waypoint[1] += int(distance)


def F(distance):
    global coordinates
    coordinates = [coordinates[0] * distance, coordinates[1] * distance]


def R(degrees):
    print('moving ' + str(degrees) + ' to the right')
    global waypoint
    if wind_direction == 0:
        pass
    elif wind_direction == 90:
        waypoint = [waypoint[1], waypoint[0]]
    elif wind_direction == 180:
        waypoint = [waypoint[0], waypoint[1]]
    elif wind_direction == 270:
        pass


def L(degrees):
    print('moving ' + str(degrees) + ' to the left')
    global wind_direction
    wind_direction = (wind_direction + int(degrees)) % 360
    if wind_direction == 0:
        N(distance)
    elif wind_direction == 90:
        W(distance)
    elif wind_direction == 180:
        S(distance)
    elif wind_direction == 270:
        E(distance)


def move(direction):
    switcher = {
        'N': N,
        'S': S,
        'E': E,
        'W': W,
        'F': F,
        'R': R,
        'L': L
    }
    func = switcher.get(direction[0])
    func(direction[1:])


def main():
    filename = 'testinput'
    directions = []
    with open(filename, 'r') as fh:
        for line in fh.readlines():
            directions.append(line.strip())
    for direction in directions:
        move(direction)
        print(coordinates)
    print(abs(coordinates[0]) + abs(coordinates[1]))


if __name__ == '__main__':
    coordinates = [0, 0]
    waypoint = [10, 1]
    wind_direction = 270
    main()
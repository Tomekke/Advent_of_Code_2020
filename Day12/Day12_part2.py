import math


def calculate_vector(degrees):
    global waypoint
    x, y = waypoint
    angle = math.acos(x/math.sqrt(x ** 2 + y ** 2))
    # angle = (y/abs(y)) * math.acos(x/math.sqrt(x ** 2 + y ** 2))
    # angle = math.atan(y/x)
    # if x < 0:
    #     angle = math.radians(180) - abs(angle)
    if y < 0:
        angle = -angle

    waypoint[0] = int(round(math.sqrt(x ** 2 + y ** 2) * math.cos(angle + math.radians(int(degrees)))))
    waypoint[1] = int(round(math.sqrt(x ** 2 + y ** 2) * math.sin(angle + math.radians(int(degrees)))))


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
    print('moving ' + distance + ' forward')
    global coordinates
    coordinates = [coordinates[0] + waypoint[0] * int(distance), coordinates[1] + waypoint[1] * int(distance)]


def R(degrees):
    print('moving ' + degrees + ' to the right')
    calculate_vector(degrees)


def L(degrees):
    print('moving ' + str(degrees) + ' to the left')
    calculate_vector(360-int(degrees))


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
    filename = 'inputfile'
    directions = []
    with open(filename, 'r') as fh:
        for line in fh.readlines():
            directions.append(line.strip())
    for direction in directions:
        move(direction)
        print(coordinates)
        print(waypoint)
    print(abs(coordinates[0]) + abs(coordinates[1]))


if __name__ == '__main__':
    coordinates = [0, 0]
    waypoint = [-10, 1]
    wind_direction = 270
    main()

def read_file_to_list(file):
    with open(file, 'r') as fh:
        numbers = []
        for line in fh.readlines():
            numbers.append(int(line))
        return numbers


def search_2_numbers(number_list, total_number):
    for number in number_list:
        second_number = total_number - number
        if second_number in number_list:
            return [number, second_number]
        # number_list.remove(number)


def search_3_numbers(number_list, total_number):
    for number in number_list:
        rest_number = total_number - number
        results = search_2_numbers(number_list, rest_number)
        if results:
            return [number, results[0], results[1]]


def multiply_list(nbr_list):
    result = 1
    for x in nbr_list:
        result = result * x
    return result

def start_here():
    filename = "inputfile"
    lines = read_file_to_list(filename)
    # Part 1
    # print(multiply_list(search_2_numbers(lines, 2020)))
    # Part 2
    print(multiply_list(search_3_numbers(lines, 2020)))


if __name__ == '__main__':
    start_here()

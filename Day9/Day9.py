"""
PART 2
"""
def sum_up_array(input_array):
    answer_num = 0
    for i in input_array:
        answer_num += i
    return answer_num


def find_cont_set(input_array, input_number):
    for index in range(0, len(input_array)):
        answer_array = []
        for number in input_array[index:]:
            answer_array.append(number)
            if sum_up_array(answer_array) == input_number:
                return answer_array
            elif sum_up_array(answer_array) > input_number:
                break


"""
PART 1
"""
def parse_array(input_array, preamble_length):
    result_array = []
    for i in range(preamble_length, len(input_array)):
        number_to_check = input_array[i]
        for number in input_array[i-preamble_length:i]:
            second_number = number_to_check - number
            if second_number >= 0:
                if second_number in input_array[i-preamble_length:i] and second_number != number:
                    result_array.append(number_to_check)
                    break
    for number in input_array[preamble_length:]:
        if number not in result_array:
            return number


def main():
    filename = 'inputfile.txt'
    preamble_length = 25
    input_array = []
    with open(filename, 'r') as fh:
        for line in fh.readlines():
            input_array.append(int(line.strip()))
    result_array = find_cont_set(input_array, parse_array(input_array, preamble_length))
    print(sorted(result_array)[0] + sorted(result_array)[-1])


if __name__ == '__main__':
    main()

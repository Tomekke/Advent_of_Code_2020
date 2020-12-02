

def check_password(min_number, max_number, letter, password):
    return True if min_number <= password.count(letter) <= max_number else False

def check_password_2(min_number, max_number, letter, password):
    # XOR
    return True if (password[min_number] == letter) != (password[max_number] == letter) else False

def main():
    filename = "inputfile"
    count = 0
    with open(filename, 'r') as fh:
        for line in fh:
            policy, password = line.split(':')
            numbers, letter = policy.split(' ')
            min_number, max_number = numbers.split('-')
            # Part 1
            # if check_password(int(min_number), int(max_number), letter, password):
            #     count += 1
            # Part 2
            if check_password_2(int(min_number), int(max_number), letter, password):
                count += 1
    print(count)


if __name__ == '__main__':
    main()
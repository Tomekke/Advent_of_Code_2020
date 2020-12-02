

def check_password(min_number, max_number, letter, password):
    print(password)
    print(password.count(letter))


def main():
    filename = "testfile"
    with open(filename, 'r') as fh:
        for line in fh:
            policy, password = line.split(':')
            numbers, letter = policy.split(' ')
            min_number, max_number = numbers.split('-')
            check_password(min_number, max_number, letter, password)


if __name__ == '__main__':
    main()
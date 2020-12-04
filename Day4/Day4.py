
def read_input(filename):
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        passport, passports = '', []
        for line in lines:
            if line != '\n':
                passport += line.replace('\n', ' ')
            else:
                passports.append(passport.strip())
                passport = ''
    return passports


def generate_dict(passports):
    for index, passport in enumerate(passports):
        testdic = {}
        for item in passport.split(' '):
            key, value = item.split(':')
            testdic[key] = value
        passports[index] = testdic
    return passports


def check_passports(passports):
    for passport in passports:
        print(passport)
        if len(passport) >= 7:
            print('yes')


def main():
    filename = 'testfile'
    check_passports(generate_dict(read_input(filename)))


if __name__ == '__main__':
    main()
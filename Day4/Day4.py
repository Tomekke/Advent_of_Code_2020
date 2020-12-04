import re

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
        passports.append(passport.strip())
    return passports


def generate_dict(passports):
    for index, passport in enumerate(passports):
        testdic = {}
        for item in passport.split(' '):
            key, value = item.split(':')
            testdic[key] = value
        passports[index] = testdic
    return passports


def passport_validation(passport):
    score = 0
    if 1920 <= int(passport['byr']) <= 2002:
        score += 1
    if 2010 <= int(passport['iyr']) <= 2020:
        score += 1
    if 2020 <= int(passport['eyr']) <= 2030:
        score += 1
    if re.match('\d+cm$', passport['hgt']):
        if 150 <= int(passport['hgt'][:-2]) <= 193:
            score += 1
    elif re.match('\d+in$', passport['hgt']):
        if 59 <= int(passport['hgt'][:-2]) <= 76:
            score += 1
    if re.match('^#[0-9a-f]{6}$', passport['hcl']) is not None:
        score += 1
    if re.match('^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$', passport['ecl']) is not None:
        score += 1
    if re.match('^\d{9}$', passport['pid']) is not None:
        score += 1

    return True if score == 7 else False


def check_passports(passports):
    correct_passports = 0
    for passport in passports:
        if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport):
            """
            Day 1
            """
            # correct_passports += 1
            """
            Day 2
            """
            if passport_validation(passport):
                correct_passports += 1
    print(correct_passports)


def main():
    filename = 'inputfile'
    check_passports(generate_dict(read_input(filename)))


if __name__ == '__main__':
    main()
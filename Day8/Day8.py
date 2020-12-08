
def check_instructions(lines):
    counter, accumulator = 0, 0
    counters_used = []
    while counter < len(lines):
        if counter not in counters_used:
            counters_used.append(counter)
            instruction, amount = lines[counter].strip().split(' ')
            if instruction == 'acc':
                accumulator += int(amount)
                counter += 1
            elif instruction == 'jmp':
                counter += int(amount)
            elif instruction == 'nop':
                counter += 1
            else:
                print('Unknown operation')
        else:
            return accumulator


def main():
    filename='inputfile'
    with open(filename, 'r') as fh:
        lines = fh.readlines()
    print(check_instructions(lines))


if __name__ == '__main__':
    main()
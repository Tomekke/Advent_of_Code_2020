
def parse_answers(answers):
    total = 0
    for answer in answers:
        total += len(set(answer))
    return total


def main():
    filename = 'inputfile'
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        answer, answers = '', []
        for line in lines:
            if line != '\n':
                answer += line.replace('\n', '')
            else:
                answers.append(answer.strip())
                answer = ''
        answers.append(answer.strip())
    print(parse_answers(answers))


if __name__ == '__main__':
    main()
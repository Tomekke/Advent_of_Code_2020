
def parse_answers(answers):
    total = 0
    for answer in answers:
        total += len(set(answer))
    return total


def parse_answers_2(answers_col):
    total = 0
    for answers in answers_col:
        yes = []
        sticked_answers = []
        for answer in answers:
            sticked_answers += answer
        for char in sticked_answers:
            if sticked_answers.count(char) == len(answers):
                yes.append(char)
        total += len(set(yes))
    return total


def main():
    filename = 'inputfile'
    """
    Day 1
    """
    # with open(filename, 'r') as fh:
    #     lines = fh.readlines()
    #     answer, answers = '', []
    #     for line in lines:
    #         if line != '\n':
    #             answer += line.replace('\n', '')
    #         else:
    #             answers.append(answer.strip())
    #             answer = ''
    #     answers.append(answer.strip())
    # print(parse_answers(answers))
    """
    Day 2
    """
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        answer, answers = [], []
        for line in lines:
            if line != '\n':
                answer.append(line.strip())
            else:
                answers.append(answer)
                answer = []
        answers.append(answer)
    print(parse_answers_2(answers))


if __name__ == '__main__':
    main()
from sys import argv


def main(
    problem_input: str,
):
    pass


if __name__ == '__main__':
    # TODO: Maybe allow for input from stdin
    input_file = 'aoc_input.txt'

    if len(argv) > 1:
        input_file = argv[1]

    with open(input_file, 'r') as f:
        problem_input = f.read()
        print(main(problem_input))

from sys import argv


def part_1(
    problem_input: str,
):
    left_list: list[int] = []
    right_list: list[int] = []

    for line in problem_input.split('\n'):
        l_id, r_id = map(int, line.split())

        left_list.append(l_id)
        right_list.append(r_id)

    left_list.sort()
    right_list.sort()

    return sum(
        map(
            lambda x: abs(x[0] - x[1]),
            zip(left_list, right_list)
        ),
    )


if __name__ == '__main__':
    # TODO: Maybe allow for input from stdin
    input_file = '01/aoc_input.txt'

    if len(argv) > 1:
        input_file = argv[1]

    with open(input_file, 'r') as f:
        problem_input = f.read()
        print(part_1(problem_input))

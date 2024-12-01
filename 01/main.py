import sys


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


def part_2(
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

    total = 0
    for l_id in left_list:
        freq = right_list.count(l_id)
        total += l_id * freq

    return total


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'part',
        help='The part of the challenge to run',
        type=int,
        choices=[1, 2],
    )
    parser.add_argument(
        '-i',
        '--input',
        '--input_file',
        type=argparse.FileType('r'),
        help='The file to use as input (if not specified stdin will be used instead)',
        nargs='?',
        default=sys.stdin,
    )

    args = parser.parse_args()

import sys


def base_part(
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
    return left_list, right_list


def part_1(
    problem_input: str,
):
    left_list, right_list = base_part(problem_input)

    return sum(
        map(
            lambda x: abs(x[0] - x[1]),
            zip(left_list, right_list)
        ),
    )


def part_2(
    problem_input: str,
):
    left_list, right_list = base_part(problem_input)

    return sum(
        l_id * right_list.count(l_id)
        for l_id in left_list
    )


if __name__ == '__main__':
    import argparse
    from typing import TextIO

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
    current_part: int = args.part
    input_file: TextIO = args.input

    parts = [part_1, part_2]
    part_func = parts[current_part - 1]

    with input_file as input_file:
        print(part_func(input_file.read().strip()))

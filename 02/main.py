import sys


def part_1(
    problem_input: str,
) -> int:
    ...


def part_2(
    problem_input: str,
) -> int:
    ...


def main():
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


if __name__ == '__main__':
    main()

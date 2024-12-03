import sys
import re


def part_1(
    problem_input: str,
) -> int:
    regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)', re.MULTILINE)

    return sum(
        int(match.group(1)) * int(match.group(2))
        for match in regex.finditer(problem_input)
    )


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

import sys
import re


def part_1(
    problem_input: str,
) -> int:
    '''
    Return the sum of the products of the two numbers in each mul call in the input.

    * Numbers are represented as 1-3 digit integers.
    * The mul calls are in the form
    `mul(x,y)` where x and y are integers. Any other form of mul call will not be considered.

    Args:
        problem_input (str): The input to process

    Returns:
        int: The sum of the products of the two numbers in each mul call in the input

    Example:
        >>> part_1("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
        161
    '''
    regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)', re.MULTILINE)

    return sum(
        int(match.group(1)) * int(match.group(2))
        for match in regex.finditer(problem_input)
    )


def part_2(
    problem_input: str,
) -> int:
    '''
    Processes the given problem input string and calculates a result based on specific patterns.

    The function uses regular expressions to find and process specific patterns in the input string:
    - "mul(lhs,rhs)": Multiplies lhs and rhs (both 1-3 digit integers) and adds the result to the total if the current state allows.
    - "do()": Sets the state to allow multiplication.
    - "don't()": Sets the state to disallow multiplication.

    Args:
        problem_input (str): The input string containing the patterns to be processed.

    Returns:
        int: The calculated result based on the processed patterns.

    Raises:
        ValueError: If an unexpected match is found in the input string.

    Example:
        >>> part_2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
        48
    '''
    regex = r"(?P<mul>mul)\((?P<lhs>\d{1,3}),(?P<rhs>\d{1,3})\)|(?P<do>do)\(\)|(?P<dont>don't)\(\)"
    result = 0
    should_do = True

    for m in re.finditer(regex, problem_input, re.MULTILINE):
        if m.group('mul') and should_do:
            result += int(m.group('lhs')) * int(m.group('rhs'))
        elif m.group('do'):
            should_do = True
        elif m.group("dont"):
            should_do = False
        else:
            raise ValueError(f"Unexpected match: {m}")

    return result


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

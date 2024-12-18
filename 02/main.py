import sys


def get_reports(
    problem_input: str,
) -> list[list[int]]:
    return [
        list(map(int, report.split()))
        for report in problem_input.split('\n')
    ]


def is_report_safe(
    report: list[int],
) -> bool:
    prev_level = report[0]
    should_increase = report[1] > report[0]

    for level in report[1:]:
        differ = 1 <= abs(level - prev_level) <= 3
        if not differ:
            return False

        if (should_increase and level > prev_level) or \
                (not should_increase and level < prev_level):
            prev_level = level
            continue

        return False

    return True


def part_1(
    problem_input: str,
) -> int:
    reports = get_reports(problem_input)

    # We could use a filter here, but it would be less readable (imho)
    return len(
        [
            report
            for report in reports
            if is_report_safe(report)
        ]
    )


def part_2(
    problem_input: str,
) -> int:
    reports = get_reports(problem_input)

    safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            safe_reports += 1
            continue

        # By removing a single element from the report, we can check if it's safe
        for i in range(len(report)):
            if is_report_safe(report[:i] + report[i + 1:]):
                safe_reports += 1
                break

    return safe_reports


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

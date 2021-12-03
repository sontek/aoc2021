import os
import argparse
import pytest

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")


def count_bit_on_index(data, index):
    zero = 0
    one = 0
    for i in range(len(data)):
        if data[i][index] == "0":
            zero += 1
        else:
            one += 1
    if zero > one:
        return ("0", "1")
    elif one > zero:
        return ("1", "0")
    else:
        return ("1", "0")


def get_common_line(data, comparator=0):
    length = len(data[0])

    for i in range(length):
        final_data = []
        commons = count_bit_on_index(data, i)
        common = commons[comparator]

        for row in data:
            if row[i] == common:
                final_data.append(row)

        data = final_data

        if len(data) == 1:
            return data[0]


def compute(data):
    o2_data = get_common_line(data)
    co2_data = get_common_line(data, 1)

    return int(o2_data, 2) * int(co2_data, 2)


TEST_INPUTS1 = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

with open(default_file) as f:
    TEST_INPUTS2 = f.read()


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        (TEST_INPUTS1, 230),
        (TEST_INPUTS2, 4105235),
    ),
)
def test_compute(input_s, expected):
    result = compute(input_s.strip().split("\n"))
    assert result == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f")
    args = parser.parse_args()

    with open(args.f or default_file) as f:
        # don't use readlines because it leaves the
        # new lines in the output.  Which throws off
        # character count.
        # lines = f.readlines()
        lines = f.read().split("\n")
        print(compute(lines))

    return 0


if __name__ == "__main__":
    exit(main())

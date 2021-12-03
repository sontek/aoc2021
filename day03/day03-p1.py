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
    else:
        return ("1", "0")


def compute(data):
    epsilon = ""
    gamma = ""
    length = len(data[0])
    for i in range(length):
        gamma += count_bit_on_index(data, i)[0]
        epsilon += count_bit_on_index(data, i)[1]

    return int(gamma, 2) * int(epsilon, 2)


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
        (TEST_INPUTS1, 198),
        (TEST_INPUTS2, 3847100),
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

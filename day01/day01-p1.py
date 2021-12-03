import os
import re
import argparse
import pytest

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")


def compute(data):
    count = 0
    for i in range(0, len(data)-1):
        one = int(data[i].strip())
        two = int(data[i+1].strip())

        if one < two:
            count += 1

    return count


TEST_INPUTS1 = '''\
199
200
208
210
200
207
240
269
260
263
'''

with open(default_file) as f:
    TEST_INPUTS2 = f.read()

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (TEST_INPUTS1, 7),
        (TEST_INPUTS2, 1548),
    ),
)
def test_compute(input_s, expected):
    result = compute(input_s.strip().split("\n"))
    assert result == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f')
    args = parser.parse_args()

    with open(args.f or default_file) as f:
        # don't use readlines because it leaves the
        # new lines in the output.  Which throws off
        # character count.
        # lines = f.readlines()
        lines = f.read().split("\n")
        print(compute(lines))

    return 0


if __name__ == '__main__':
    exit(main())

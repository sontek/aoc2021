import os
import argparse
import pytest

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")


def compute(data):
    h = 0
    d = 0
    aim = 0

    for i in range(0, len(data)):
        cmd, value = data[i].strip().split()
        value = int(value)
        if cmd == 'forward':
            h += value
            d += aim * value
        elif cmd == 'up':
            aim -= value
        elif cmd == 'down':
            aim += value

    return h * d


TEST_INPUTS1 = '''\
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''

with open(default_file) as f:
    TEST_INPUTS2 = f.read()


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (TEST_INPUTS1, 900),
        (TEST_INPUTS2, 1975421260),
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

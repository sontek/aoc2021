import os
import argparse
import pytest

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")


def compute(data):
    count = 0
    first_index = 0
    second_index = 1

    one = int(data[first_index].strip())
    two = int(data[first_index+1].strip())
    three = int(data[first_index+2].strip())
    previous = one + two + three

    for i in range(0, len(data)):
        if second_index + 2 > len(data) - 1:
            break

        four = int(data[second_index].strip())
        five = int(data[second_index+1].strip())
        six = int(data[second_index+2].strip())
        second_total = four + five + six

        print(previous, second_total)
        if previous < second_total:
            count += 1

        previous = second_total
        second_index += 1

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
        (TEST_INPUTS1, 5),
        (TEST_INPUTS2, 1589),
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

import os
import argparse
import pytest
from collections import defaultdict

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")


def compute(data):
    coords = []

    for line in data:
        line_coords = []
        start, end = line.split(" -> ")
        startx, starty = [int(x) for x in start.split(",")]
        endx, endy = [int(y) for y in end.split(",")]
        xargs = sorted([startx, endx])
        yargs = sorted([starty, endy])

        # only grab straight lines
        if startx == endx or starty == endy:
            for x in range(xargs[0], xargs[1] + 1):
                for y in range(yargs[0], yargs[1] + 1):
                    line_coords.append((x, y))

            coords.append(line_coords)

    seen_coords = defaultdict(int)
    for line in coords:
        for coord in line:
            seen_coords[coord] += 1

    return len([x for x in seen_coords.values() if x >= 2])


TEST_INPUTS1 = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

with open(default_file) as f:
    TEST_INPUTS2 = f.read()


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        (TEST_INPUTS1, 5),
        (TEST_INPUTS2, 6564),
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

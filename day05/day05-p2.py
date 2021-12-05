import os
import argparse
import pytest
from collections import defaultdict

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")


def full_range(start: int, end: int):
    data = list(range(start, end, 1 if start <= end else -1))
    data.append(end)
    return data


def compute(data):
    coords = []

    for line in data:
        line_coords = []
        start, end = line.split(" -> ")
        startx, starty = [int(x) for x in start.split(",")]
        endx, endy = [int(y) for y in end.split(",")]
        x1, x2 = sorted([startx, endx])
        y1, y2 = sorted([starty, endy])
        # only grab straight lines
        if startx == endx or starty == endy:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    line_coords.append((x, y))
        else:
            slope = (starty - endy) / (startx - endx)
            # diagonal
            # 8,0 -> 0,8 /    max_x=8, min_x=0, max_y=8, min_y=0
            # 6,4 -> 2,0 \    max_x=6, min_x=2, max_y=4, min_y=0
            # 0,0 -> 8,8 \    max_x=8, min_x=0, max_y=8, min_y=0
            # 5,5 -> 8,2 /    max_x=8, min_x=5, max_y-5, min_y=2
            # /

            # Flip the starts and ends if the endy is less than the
            # start.
            if endy < starty:
                startx, starty, endx, endy = endx, endy, startx, starty

            while starty <= endy:
                line_coords.append((startx, starty))
                startx += slope
                starty += 1

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
        (TEST_INPUTS1, 12),
        (TEST_INPUTS2, 19172),
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

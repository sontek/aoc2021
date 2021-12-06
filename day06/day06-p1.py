import os
import argparse
import pytest
from collections import defaultdict

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")


def compute(data):
    fishies = defaultdict(int)
    for init in data[0].split(","):
        fishies[int(init)] += 1

    for i in range(80):
        new_fishies = 0
        for j in range(9):
            if j == 0:
                if fishies[0] > 0:
                    new_fishies = fishies[0]
                    fishies[0] = 0
            else:
                if fishies[j] > 0:
                    fishies[j - 1] += fishies[j]
                    fishies[j] -= fishies[j]

        fishies[6] += new_fishies
        fishies[8] += new_fishies

    return sum(fishies.values())


TEST_INPUTS1 = """\
3,4,3,1,2
"""

with open(default_file) as f:
    TEST_INPUTS2 = f.read()


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        (TEST_INPUTS1, 5934),
        # (TEST_INPUTS2, 393019),
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

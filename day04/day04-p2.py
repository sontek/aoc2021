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


def calculate_winning_combos():
    horizontals = []
    verticals = []
    current = 0

    # calculate the winning combos for horizontal
    for i in range(5):
        horizontal = []
        vertical = []
        for j in range(current, current + 5):
            horizontal.append(j)
        for j in range(i, i + 25, 5):
            vertical.append(j)
        horizontals.append(horizontal)
        verticals.append(vertical)

        current += 5

    return horizontals + verticals


def make_boards(lines):
    boards = []
    current_board = []

    for row in lines:
        row = row.strip()
        if row == "":
            boards.append(current_board)
            current_board = []
        else:
            numbers = [int(x) for x in row.split(" ") if x != ""]
            current_board += numbers

    boards.append(current_board)
    return boards


WINNING_RESULT = ["X"] * 5


def get_winner(winning_combos, board):
    for row in winning_combos:
        result = [board[i] for i in row]
        if result == WINNING_RESULT:
            return True

    return False


def compute(randoms, boards):
    winning_combos = calculate_winning_combos()
    winners = []
    for next_number in randoms:
        for index, board in enumerate(boards):
            number_index = -1
            try:
                number_index = board.index(next_number)
            except ValueError:
                # just means the number isn't present.
                pass

            if number_index >= 0:
                board[number_index] = "X"
                is_winner = get_winner(winning_combos, board)
                if is_winner:
                    if index not in winners:
                        winners.append(index)
                    if len(winners) == len(boards):
                        score = sum(x for x in board if x != "X") * next_number
                        return score
    return 0


TEST_INPUTS1 = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

with open(default_file) as f:
    TEST_INPUTS2 = f.read()


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        (TEST_INPUTS1, 1924),
        (TEST_INPUTS2, 19012),
    ),
)
def test_compute(input_s, expected):
    data = input_s.strip().split("\n")
    randoms = [int(x) for x in data[0].split(",")]
    lines = make_boards(data[2:])
    result = compute(randoms, lines)
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
        data = f.read().split("\n")
        randoms = [int(x) for x in data[0].split(",")]
        lines = make_boards(data[2:])
        print(compute(randoms, lines))

    return 0


if __name__ == "__main__":
    exit(main())

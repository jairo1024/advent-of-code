from aoc import utils
from aoc.year_2022 import day04


def test_part1():
    ids = utils.readlines_from_file("resources/year_2022/day04.txt")

    count = day04.part1(ids)

    assert count == 526

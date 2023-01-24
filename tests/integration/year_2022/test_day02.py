from aoc import utils
from aoc.year_2022 import day02


def test_part1():
    rounds = utils.readlines_from_file("resources/year_2022/day02.txt")

    score = day02.part1(rounds)

    assert score == 8392


def test_part2():
    rounds = utils.readlines_from_file("resources/year_2022/day02.txt")

    score = day02.part2(rounds)

    assert score == 10116

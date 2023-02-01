from aoc import utils
from aoc.year_2022 import day03


def test_part1():
    rucksacks = utils.readlines_from_file("resources/year_2022/day03.txt")

    sum = day03.part1(rucksacks)

    assert sum == 7746


def test_part2():
    rucksacks = utils.readlines_from_file("resources/year_2022/day03.txt")

    sum = day03.part2(rucksacks)

    assert sum == 2604

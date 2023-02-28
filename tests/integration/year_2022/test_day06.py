from aoc import utils
from aoc.year_2022 import day06


def test_part1():
    datastream = utils.read_from_file("resources/year_2022/day06.txt")

    marker = day06.part1(datastream)

    assert marker == 1929


def test_part2():
    datastream = utils.read_from_file("resources/year_2022/day06.txt")

    marker = day06.part2(datastream)

    assert marker == 3298

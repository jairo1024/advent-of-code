from aoc import utils
from aoc.year_2022 import day05


def test_part1():
    stack_strings = utils.readlines_from_file("resources/year_2022/day05.txt")

    top_of_stacks = day05.part1(stack_strings)

    assert top_of_stacks == "CVCWCRTVQ"


def test_part2():
    stack_strings = utils.readlines_from_file("resources/year_2022/day05.txt")

    top_of_stacks = day05.part2(stack_strings)

    assert top_of_stacks == "CNSCZWLVT"

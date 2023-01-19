from aoc import utils
from aoc.year_2022 import day01

def test_part1():
    calorie_inventory = utils.readlines_from_file("resources/year_2022/day01_part1.txt")

    calories = day01.part1(calorie_inventory)

    assert calories == 72240

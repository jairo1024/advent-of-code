from aoc.year_2022 import day03


class TestGetRucksackPrioritySum:
    def test_no_duplicate_items(self):
        expected_sum = 0
        rucksack = "jv"

        sum = day03.get_rucksack_priority_sum(rucksack)

        assert sum == expected_sum

    def test_1_lowercase_item(self):
        expected_sum = 2
        rucksack = "abbc"

        sum = day03.get_rucksack_priority_sum(rucksack)

        assert sum == expected_sum

    def test_multiple_lowercase_items(self):
        expected_sum = 15
        rucksack = "abcdeffedxyz"

        sum = day03.get_rucksack_priority_sum(rucksack)

        assert sum == expected_sum

    def test_1_uppercase_item(self):
        expected_sum = 27
        rucksack = "AA"

        sum = day03.get_rucksack_priority_sum(rucksack)

        assert sum == expected_sum

    def test_multiple_uppercase_items(self):
        expected_sum = 93
        rucksack = "abcDEFFEDxyz"

        sum = day03.get_rucksack_priority_sum(rucksack)

        assert sum == expected_sum

    def test_mix_of_uppercase_and_lower_case_items(self):
        expected_sum = 32
        rucksack = "aBcdzdBx"

        sum = day03.get_rucksack_priority_sum(rucksack)

        assert sum == expected_sum

    def test_multiple_of_the_same_item_are_counted_only_once(self):
        expected_sum = 28
        rucksack = "aBBBczBBBx"

        sum = day03.get_rucksack_priority_sum(rucksack)

        assert sum == expected_sum


class TestPart1:
    def test_sum_of_one_rucksack(self):
        expected_sum = 2
        rucksacks = ["abbc"]

        sum = day03.part1(rucksacks)

        assert sum == expected_sum

    def test_sum_of_multiple_rucksacks(self):
        expected_sum = 29
        rucksacks = ["abbc", "AA"]

        sum = day03.part1(rucksacks)

        assert sum == expected_sum

    def test_sum_of_given_example(self):
        expected_sum = 157
        rucksacks = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]

        sum = day03.part1(rucksacks)

        assert sum == expected_sum

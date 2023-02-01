from aoc.year_2022 import day03


class TestGetRucksackPrioritySum:
    def test_no_duplicate_items(self):
        expected_sum = 0
        left_rucksack = "j"
        right_rucksack = "v"

        sum = day03.get_rucksack_priority_sum(left_rucksack, right_rucksack)

        assert sum == expected_sum

    def test_1_lowercase_item(self):
        expected_sum = 2
        left_rucksack = "ab"
        right_rucksack = "bc"

        sum = day03.get_rucksack_priority_sum(left_rucksack, right_rucksack)

        assert sum == expected_sum

    def test_multiple_lowercase_items(self):
        expected_sum = 15
        left_rucksack = "abcdef"
        right_rucksack = "fedxyz"

        sum = day03.get_rucksack_priority_sum(left_rucksack, right_rucksack)

        assert sum == expected_sum

    def test_1_uppercase_item(self):
        expected_sum = 27
        left_rucksack = "A"
        right_rucksack = "A"

        sum = day03.get_rucksack_priority_sum(left_rucksack, right_rucksack)

        assert sum == expected_sum

    def test_multiple_uppercase_items(self):
        expected_sum = 93
        left_rucksack = "abcDEF"
        right_rucksack = "FEDxyz"

        sum = day03.get_rucksack_priority_sum(left_rucksack, right_rucksack)

        assert sum == expected_sum

    def test_mix_of_uppercase_and_lower_case_items(self):
        expected_sum = 32
        left_rucksack = "aBcd"
        right_rucksack = "zdBx"

        sum = day03.get_rucksack_priority_sum(left_rucksack, right_rucksack)

        assert sum == expected_sum

    def test_multiple_of_the_same_item_are_counted_only_once(self):
        expected_sum = 28
        left_rucksack = "aBBBc"
        right_rucksack = "zBBBx"

        sum = day03.get_rucksack_priority_sum(left_rucksack, right_rucksack)

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


class TestPart2:
    def test_sum_of_one_set(self):
        expected_sum = 18
        rucksacks = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
        ]

        sum = day03.part2(rucksacks)

        assert sum == expected_sum

    def test_sum_of_multiple_sets(self):
        expected_sum = 70
        rucksacks = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]

        sum = day03.part2(rucksacks)

        assert sum == expected_sum

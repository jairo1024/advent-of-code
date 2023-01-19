from aoc.year_2022 import day01


class TestPart1:
    def test_empty_calorie_list(self):
        expected_calories = None
        calorie_inventory = []

        calories = day01.part1(calorie_inventory)

        assert calories == expected_calories

    def test_one_elf_in_calorie_list(self):
        expected_calories = 3
        calorie_inventory = ["1", "1", "1"]

        calories = day01.part1(calorie_inventory)

        assert calories == expected_calories

    def test_multiple_elfs_in_calorie_list(self):
        expected_calories = 6
        calorie_inventory = ["1", "1", "1", "", "2", "4", "", "1", "1"]

        calories = day01.part1(calorie_inventory)

        assert calories == expected_calories

    def test_last_elf_has_highest_calories_in_calorie_list(self):
        expected_calories = 5
        calorie_inventory = ["1", "1", "1", "", "2", "2", "", "3", "2"]

        calories = day01.part1(calorie_inventory)

        assert calories == expected_calories


class TestPart2:
    def test_empty_calorie_list(self):
        expected_calories = None
        calorie_inventory = []

        calories = day01.part2(calorie_inventory)

        assert calories == expected_calories

    def test_the_sum_of_top_3_elf_calories_is_returned(self):
        expected_calories = 15
        calorie_inventory = [
            "1",
            "1",
            "1",
            "",
            "2",
            "4",
            "",
            "1",
            "1",
            "",
            "2",
            "2",
            "2",
        ]

        calories = day01.part2(calorie_inventory)

        assert calories == expected_calories

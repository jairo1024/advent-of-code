from aoc.year_2022 import day04


class TestGetRange:
    def test_single_range(self):
        expected_sections = {1}
        id = "1-1"

        sections = day04.get_range(id)

        assert sections == expected_sections

    def test_multiple_ranges(self):
        expected_sections = {4, 5, 6}
        id = "4-6"

        sections = day04.get_range(id)

        assert sections == expected_sections


class TestGetSections:
    def test_one_pair(self):
        expected_sections = [{2, 3, 4}, {6, 7, 8}]
        id = "2-4,6-8"

        sections = day04.get_sections(id)

        assert sections == expected_sections

    def test_same_range_for_both_sections(self):
        expected_sections = [{1, 2, 3}, {1, 2, 3}]
        id = "1-3,1-3"

        sections = day04.get_sections(id)

        assert sections == expected_sections

    def test_one_range_for_both_sections(self):
        expected_sections = [{1}, {1}]
        id = "1-1,1-1"

        sections = day04.get_sections(id)

        assert sections == expected_sections

    def test_different_ranges_for_both_sections(self):
        expected_sections = [{4, 5, 6}, {2, 3, 4, 5}]
        id = "4-6,2-5"

        sections = day04.get_sections(id)

        assert sections == expected_sections


class TestPart1:
    def test_one_group(self):
        expected_duplicates = 0
        ids = ["2-4,6-8"]

        duplicates = day04.part1(ids)

        assert duplicates == expected_duplicates

    def test_multiple_groups(self):
        expected_duplicates = 0
        ids = ["2-4,6-8", "1-2,8-9"]

        duplicates = day04.part1(ids)

        assert duplicates == expected_duplicates

    def test_duplicate_group(self):
        expected_duplicates = 1
        ids = ["2-4,2-5", "1-2,7-8"]

        duplicates = day04.part1(ids)

        assert duplicates == expected_duplicates

    def test_provided_example(self):
        expected_duplicates = 2
        ids = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]

        duplicates = day04.part1(ids)

        assert duplicates == expected_duplicates


class TestPart2:
    def test_empty_list(self):
        expected_overlapping = 0
        ids = []

        overlapping = day04.part2(ids)

        assert overlapping == expected_overlapping

    def test_one_group_with_overlapping(self):
        expected_overlapping = 1
        ids = ["2-4,4-8"]

        overlapping = day04.part2(ids)

        assert overlapping == expected_overlapping

    def test_one_group_with_multiple_overlapping_counts_as_one(self):
        expected_overlapping = 1
        ids = ["2-5,3-6"]

        overlapping = day04.part2(ids)

        assert overlapping == expected_overlapping

    def test_multiple_groups_no_overlapping(self):
        expected_overlapping = 0
        ids = ["2-4,6-8", "2-3,4-5"]

        overlapping = day04.part2(ids)

        assert overlapping == expected_overlapping

    def test_multiple_groups_with_overlapping(self):
        expected_overlapping = 3
        ids = ["1-4,3-8", "2-3,3-5", "1-4,6-8", "7-9,8-9"]

        overlapping = day04.part2(ids)

        assert overlapping == expected_overlapping

    def test_provided_example(self):
        expected_duplicates = 4
        ids = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]

        duplicates = day04.part2(ids)

        assert duplicates == expected_duplicates

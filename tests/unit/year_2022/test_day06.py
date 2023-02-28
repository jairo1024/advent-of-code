from aoc.year_2022 import day06
import pytest


class TestFindMarker:
    def test_1_unique_sequence(self):
        datastream = "abcd"
        sequence_amount = 1
        expected_marker = 1

        marker = day06.find_marker(datastream, sequence_amount)

        assert marker == expected_marker

    def test_2_unique_sequence(self):
        datastream = "abcd"
        sequence_amount = 2
        expected_marker = 2

        marker = day06.find_marker(datastream, sequence_amount)

        assert marker == expected_marker

    def test_3_unique_sequence(self):
        datastream = "abcd"
        sequence_amount = 3
        expected_marker = 3

        marker = day06.find_marker(datastream, sequence_amount)

        assert marker == expected_marker

    def test_duplicate_datastreams_in_sequence(self):
        datastream = "abbcdef"
        sequence_amount = 3
        expected_marker = 5

        marker = day06.find_marker(datastream, sequence_amount)

        assert marker == expected_marker

    @pytest.mark.parametrize(
        "datastream, sequence_amount, expected_marker",
        [
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 4, 5),
            ("nppdvjthqldpwncqszvftbrmjlhg", 4, 6),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4, 10),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4, 11),
        ],
    )
    def test_provided_example(self, datastream, sequence_amount, expected_marker):

        marker = day06.find_marker(datastream, sequence_amount)

        assert marker == expected_marker


class TestPart1:
    @pytest.mark.parametrize(
        "datastream, expected_marker",
        [
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
            ("nppdvjthqldpwncqszvftbrmjlhg", 6),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
        ],
    )
    def test_provided_example(self, datastream, expected_marker):

        marker = day06.part1(datastream)

        assert marker == expected_marker

from aoc.year_2022.day07.file import File
from aoc.year_2022.day07.folder import Folder
import pytest


class TestFileClass:
    @pytest.mark.parametrize(
        "raw_input, expected_name",
        [
            ("100 a.txt", "a.txt"),
            ("99 b.txt", "b.txt"),
        ],
    )
    def test_file_name_can_be_parsed(self, raw_input, expected_name):
        file = File(Folder("folder_name"), raw_input)

        name = file.get_name()

        assert name == expected_name

    @pytest.mark.parametrize(
        "raw_input, expected_size",
        [
            ("100 a.txt", 100),
            ("99 b.txt", 99),
        ],
    )
    def test_file_size_can_be_parsed(self, raw_input, expected_size):
        file = File(Folder("folder_name"), raw_input)

        size = file.get_size()

        assert size == expected_size

    def test_file_name_parent(self):
        raw_input = "100 a.txt"
        parent_folder = Folder("folder_name")
        file = File(parent_folder, raw_input)

        parent = file.get_parent()

        assert parent == parent_folder

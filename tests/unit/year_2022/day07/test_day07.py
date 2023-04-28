from aoc.year_2022.day07.day07 import *
import pytest


class TestGenerateTree:
    def test_cd_root(self, capfd):
        #        expected_tree = (
        #        'root - 48381165 bytes (Dir)\n'
        #        '|___ b.txt - 14848514 bytes (File)\n'
        #        '|___ c.dat - 8504156 bytes (File)\n'
        #        '|___ a - 94853 bytes (Dir)\n'
        #        '     |___ f - 29116 bytes (File)\n'
        #        '     |___ g - 2557 bytes (File)\n'
        #        '     |___ h.lst - 62596 bytes (File)\n'
        #        '     |___ e - 584 bytes (Dir)\n'
        #        '          |___ i - 584 bytes (File)\n'
        #        '|___ d - 24933642 bytes (Dir)\n'
        #        '     |___ j - 4060174 bytes (File)\n'
        #        '     |___ d.log - 8033020 bytes (File)\n'
        #        '     |___ d.ext - 5626152 bytes (File)\n'
        #        '     |___ k - 7214296 bytes (File)\n\n')
        expected_tree = "root - 0 bytes (Dir)\n\n"
        terminal_output = ["$ cd /"]

        tree = generate_tree(terminal_output)
        tree.print_tree()
        printed_tree, err = capfd.readouterr()

        assert printed_tree == expected_tree

    def test_exception_is_raised_when_tree_does_not_start_as_root(self, capfd):
        terminal_output = ["$ cd abc"]

        with pytest.raises(Exception) as exc_info:
            tree = generate_tree(terminal_output)

        assert str(exc_info.value) == "Tree is not starting with root"

    def test_create_files_in_directory(self, capfd):
        expected_tree = (
            "root - 20 bytes (Dir)\n"
            "|___ b.txt - 12 bytes (File)\n"
            "|___ c.dat - 8 bytes (File)\n\n"
        )
        terminal_output = ["$ cd /", "$ ls", "12 b.txt", "8 c.dat"]

        tree = generate_tree(terminal_output)
        tree.print_tree()
        printed_tree, err = capfd.readouterr()

        assert printed_tree == expected_tree

    def test_create_files_and_an_empty_directory(self, capfd):
        expected_tree = (
            "root - 20 bytes (Dir)\n"
            "|___ b.txt - 12 bytes (File)\n"
            "|___ c.dat - 8 bytes (File)\n"
            "|___ a - 0 bytes (Dir)\n\n"
        )
        terminal_output = ["$ cd /", "$ ls", "12 b.txt", "8 c.dat", "dir a"]

        tree = generate_tree(terminal_output)
        tree.print_tree()
        printed_tree, err = capfd.readouterr()

        assert printed_tree == expected_tree

    def test_create_files_and_a_sub_directory_with_files(self, capfd):
        expected_tree = (
            "root - 30 bytes (Dir)\n"
            "|___ b.txt - 12 bytes (File)\n"
            "|___ c.dat - 8 bytes (File)\n"
            "|___ a - 10 bytes (Dir)\n"
            "     |___ f - 5 bytes (File)\n"
            "     |___ g - 5 bytes (File)\n\n"
        )
        terminal_output = [
            "$ cd /",
            "$ ls",
            "12 b.txt",
            "8 c.dat",
            "dir a",
            "$ cd a",
            "$ ls",
            "5 f",
            "5 g",
        ]

        tree = generate_tree(terminal_output)
        tree.print_tree()
        printed_tree, err = capfd.readouterr()

        assert printed_tree == expected_tree

    def test_create_files_and_multiple_sub_directories_with_files(self, capfd):
        expected_tree = (
            "root - 42 bytes (Dir)\n"
            "|___ b.txt - 12 bytes (File)\n"
            "|___ c.dat - 8 bytes (File)\n"
            "|___ a - 10 bytes (Dir)\n"
            "     |___ f - 5 bytes (File)\n"
            "     |___ g - 5 bytes (File)\n"
            "|___ d - 12 bytes (Dir)\n"
            "     |___ j - 6 bytes (File)\n"
            "     |___ d.log - 6 bytes (File)\n\n"
        )
        terminal_output = [
            "$ cd /",
            "$ ls",
            "12 b.txt",
            "8 c.dat",
            "dir a",
            "dir d",
            "$ cd a",
            "$ ls",
            "5 f",
            "5 g",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "6 j",
            "6 d.log",
        ]

        tree = generate_tree(terminal_output)
        tree.print_tree()
        printed_tree, err = capfd.readouterr()

        assert printed_tree == expected_tree

    def test_provided_example(self, capfd):
        expected_tree = (
            "root - 48381165 bytes (Dir)\n"
            "|___ b.txt - 14848514 bytes (File)\n"
            "|___ c.dat - 8504156 bytes (File)\n"
            "|___ a - 94853 bytes (Dir)\n"
            "     |___ f - 29116 bytes (File)\n"
            "     |___ g - 2557 bytes (File)\n"
            "     |___ h.lst - 62596 bytes (File)\n"
            "     |___ e - 584 bytes (Dir)\n"
            "          |___ i - 584 bytes (File)\n"
            "|___ d - 24933642 bytes (Dir)\n"
            "     |___ j - 4060174 bytes (File)\n"
            "     |___ d.log - 8033020 bytes (File)\n"
            "     |___ d.ext - 5626152 bytes (File)\n"
            "     |___ k - 7214296 bytes (File)\n\n"
        )
        terminal_output = [
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k",
        ]

        tree = generate_tree(terminal_output)
        tree.print_tree()
        printed_tree, err = capfd.readouterr()

        assert printed_tree == expected_tree

#
# class TestPart1:
#    @pytest.mark.parametrize(
#        "datastream, expected_marker",
#        [
#            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
#            ("nppdvjthqldpwncqszvftbrmjlhg", 6),
#            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
#            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
#        ],
#    )
#    def test_provided_example(self, datastream, expected_marker):
#
#        marker = day06.part1(datastream)
#
#        assert marker == expected_marker
#
#
# class TestPart2:
#    @pytest.mark.parametrize(
#        "datastream, expected_marker",
#        [
#            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
#            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
#            ("nppdvjthqldpwncqszvftbrmjlhg", 23),
#            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
#            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
#        ],
#    )
#    def test_provided_example(self, datastream, expected_marker):
#
#        marker = day06.part2(datastream)
#
#        assert marker == expected_marker

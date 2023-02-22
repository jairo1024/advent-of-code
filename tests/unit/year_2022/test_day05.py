from aoc.year_2022 import day05
from collections import deque
import pytest


class TestGenerateStacksFromListOfStrings:
    def test_single_stack(self):
        stack_strings = [
            "[A]",
            "[B]",
            "[C]",
            " 1 ",
        ]
        stack_1 = deque(["C", "B", "A"])
        expected_stacks = {1: stack_1}

        stacks = day05.generate_stacks_from_list_of_strings(stack_strings)

        assert stacks == expected_stacks

    def test_multiple_stacks(self):
        stack_strings = [
            "[A] [V]",
            "[B] [X]",
            "[C] [Y]",
            " 1   2 ",
        ]
        stack_1 = deque(["C", "B", "A"])
        stack_2 = deque(["Y", "X", "V"])
        expected_stacks = {1: stack_1, 2: stack_2}

        stacks = day05.generate_stacks_from_list_of_strings(stack_strings)

        assert stacks == expected_stacks

    def test_uneven_stacks(self):
        stack_strings = [
            "    [V]",
            "[B] [X]",
            "[C] [Y]",
            " 1   2 ",
        ]
        stack_1 = deque(["C", "B"])
        stack_2 = deque(["Y", "X", "V"])
        expected_stacks = {1: stack_1, 2: stack_2}

        stacks = day05.generate_stacks_from_list_of_strings(stack_strings)

        assert stacks == expected_stacks


class TestParseInstruction:
    @pytest.mark.parametrize(
        "instruction_string, expected_instruction",
        [
            ("move 1 from 2 to 1", {"move": 1, "from": 2, "to": 1}),
            ("move 3 from 1 to 3", {"move": 3, "from": 1, "to": 3}),
            ("move 3 from 1 to 3", {"move": 3, "from": 1, "to": 3}),
            ("move 2 from 2 to 1", {"move": 2, "from": 2, "to": 1}),
            ("move 1 from 1 to 2", {"move": 1, "from": 1, "to": 2}),
        ],
    )
    def test_instruction_is_parsed(self, instruction_string, expected_instruction):
        instruction = None

        instruction = day05.parse_instruction(instruction_string)

        assert instruction == expected_instruction


class TestMoveStack9000:
    def test_stack_is_moved(self):
        instruction = {"move": 1, "from": 2, "to": 1}
        stacks = {1: deque(["C", "B", "A"]), 2: deque(["Y", "X", "V"])}
        expected_stacks = {1: deque(["C", "B", "A", "V"]), 2: deque(["Y", "X"])}

        updated_stacks = day05.move_stack_9000(stacks, instruction)

        assert updated_stacks == expected_stacks

    def test_multiple_crates_are_moved_from_stack(self):
        instruction = {"move": 2, "from": 2, "to": 1}
        stacks = {1: deque(["C", "B", "A"]), 2: deque(["Y", "X", "V"])}
        expected_stacks = {1: deque(["C", "B", "A", "V", "X"]), 2: deque(["Y"])}

        updated_stacks = day05.move_stack_9000(stacks, instruction)

        assert updated_stacks == expected_stacks


class TestMoveStack9001:
    def test_stack_is_moved(self):
        instruction = {"move": 1, "from": 2, "to": 1}
        stacks = {1: deque(["C", "B", "A"]), 2: deque(["Y", "X", "V"])}
        expected_stacks = {1: deque(["C", "B", "A", "V"]), 2: deque(["Y", "X"])}

        updated_stacks = day05.move_stack_9001(stacks, instruction)

        assert updated_stacks == expected_stacks

    def test_multiple_crates_are_moved_from_stack(self):
        instruction = {"move": 3, "from": 2, "to": 1}
        stacks = {1: deque(["C", "B", "A"]), 2: deque(["Z", "Y", "X", "V"])}
        expected_stacks = {1: deque(["C", "B", "A", "Y", "X", "V"]), 2: deque(["Z"])}

        updated_stacks = day05.move_stack_9001(stacks, instruction)

        assert updated_stacks == expected_stacks


class TestPart1:
    def test_one_stack_is_moved(self):
        stack_strings = [
            "[A] [V]",
            "[B] [X]",
            "[C] [Y]",
            " 1   2 ",
            "",
            "move 1 from 2 to 1",
        ]
        expected_top_of_stacks = "VX"

        top_of_stacks = day05.part1(stack_strings)

        assert top_of_stacks == expected_top_of_stacks

    def test_multiple_stacks_are_moved(self):
        stack_strings = [
            "[A] [V] [M]",
            "[B] [X] [N]",
            "[C] [Y] [O]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 2 from 1 to 3",
        ]
        expected_top_of_stacks = "BXA"

        top_of_stacks = day05.part1(stack_strings)

        assert top_of_stacks == expected_top_of_stacks

    def test_provided_example(self):
        stack_strings = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
        ]
        expected_top_of_stacks = "CMZ"

        top_of_stacks = day05.part1(stack_strings)

        assert top_of_stacks == expected_top_of_stacks


class TestPart2:
    def test_one_stack_is_moved(self):
        stack_strings = [
            "[A] [V]",
            "[B] [X]",
            "[C] [Y]",
            " 1   2 ",
            "",
            "move 1 from 2 to 1",
        ]
        expected_top_of_stacks = "VX"

        top_of_stacks = day05.part2(stack_strings)

        assert top_of_stacks == expected_top_of_stacks

    def test_multiple_stacks_are_moved(self):
        stack_strings = [
            "[A] [V] [M]",
            "[B] [X] [N]",
            "[C] [Y] [O]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 2 from 1 to 3",
        ]
        expected_top_of_stacks = "BXV"

        top_of_stacks = day05.part2(stack_strings)

        assert top_of_stacks == expected_top_of_stacks

    def test_provided_example(self):
        stack_strings = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
        ]
        expected_top_of_stacks = "MCD"

        top_of_stacks = day05.part2(stack_strings)

        assert top_of_stacks == expected_top_of_stacks

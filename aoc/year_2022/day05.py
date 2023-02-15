from collections import deque


def part1(stack_strings):
    """
    Big O: Time complexity: O(n^2) / Space complexity: O(n)
    :param stack_strings: A list of strings that contain the stacks and instructions
    :return: Returns the combination of the top of each stack

    Input:
        stack_strings: [
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

    Return:
        "CMZ"
    """
    break_index = None
    for index, value in enumerate(stack_strings):
        if not value:
            break_index = index
            break

    stacks = generate_stacks_from_list_of_strings(stack_strings[:break_index])

    for instruction in stack_strings[break_index + 1 :]:
        command = parse_instruction(instruction)
        stacks = move_stack(stacks, command)

    top_of_stacks = ""
    for index in range(len(stacks)):
        top_of_stacks = top_of_stacks + stacks[index + 1].pop()

    return top_of_stacks


def generate_stacks_from_list_of_strings(stack_strings):
    """
    Big O: Time complexity: O(n^2) / Space complexity: O(n)
    :param stack_strings: A list of strings that contain the stacks
    :return: Returns a dictionary with the stacks

    Input:
        stack_strings: [
            "[A] [V]",
            "[B] [X]",
            "[C] [Y]",
            " 1   2 ",
        ]

    Return:
        { 1 : deque(["C", "B", "A"]), 2 : deque(["Y", "X", "V"]) }

    """
    stacks = generate_empty_stacks(stack_strings)

    # Populate Stacks
    for row in reversed(stack_strings[:-1]):
        values = row.split(" ")
        sections = [row[i : i + 4] for i in range(0, len(row), 4)]
        for index, value in enumerate(sections):
            value = value.replace("[", "").replace("]", "").replace(" ", "")
            if value:
                stacks[index + 1].append(value)

    return stacks


def generate_empty_stacks(stack_strings):
    """
    Big O: Time complexity: O(n) / Space complexity: O(n)
    :param stack_strings: A list of strings that contain the stacks
    :return: Returns a dictionary of empty stacks

    Input:
        stack_strings: [
            "[A] [V]",
            "[B] [X]",
            "[C] [Y]",
            " 1   2 ",
        ]

    Return:
        { 1 : deque([]), 2 : deque([]) }

    """
    empty_stacks = {}
    # Generate Empty Stacks
    for stack in stack_strings[-1].split("   "):
        stack = int(stack.replace(" ", ""))
        empty_stacks[stack] = deque()

    return empty_stacks


def parse_instruction(instruction_string):
    """
    Big O: Time complexity: O(n) / Space complexity: O(n)
    :param instruction_string: A string that contains the instructions for the stacks
    :return: Returns a dictionary with the parsed instructions

    Input:
        instruction_string: "move 1 from 2 to 1"

    Return:
        {"move": 1, "from": 2, "to": 1}
    """
    items = iter(instruction_string.split(" "))
    return {item: int(next(items)) for item in items}


def move_stack(stacks, instruction):
    """
    Big O: Time complexity: O(n) / Space complexity: O(n)
    :param instruction_string: A string that contains the instructions for the stacks
    :return: Returns a dictionary with the parsed instructions

    Input:
        stacks: { 1 : deque(["C", "B", "A"]), 2 : deque(["Y", "X", "V"]) }

        instruction: {"move": 1, "from": 2, "to": 1}

    Return:
        { 1 : deque(["C", "B", "A", "V"]), 2 : deque(["Y", "X"]) }

    """
    for move in range(instruction["move"]):
        from_stack_id = instruction["from"]
        to_stack_id = instruction["to"]

        value = stacks[from_stack_id].pop()
        stacks[to_stack_id].append(value)

    return stacks

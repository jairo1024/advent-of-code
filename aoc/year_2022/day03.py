def part1(rucksacks):
    """
    Big O: O(n^2) / Time complexity: O(n)
    :param rucksacks: A list of the rucksack strings
    :return: Returns the total sum of all of the priority items in all of the rucksacks
    """
    total = 0
    for rucksack in rucksacks:
        left = rucksack[: len(rucksack) // 2]
        right = rucksack[len(rucksack) // 2 :]
        total += get_rucksack_priority_sum(left, right)
    return total


def part2(rucksacks):
    """
    Big O: O(n^2) / Time complexity: O(n)
    :param rucksacks: A list of the rucksack strings
    :return: Returns the total sum of the priorities between groups
    """
    total = 0
    rucksack_iter = iter(rucksacks)
    for rucksack in rucksack_iter:
        group_1 = rucksack
        group_2 = next(rucksack_iter)
        group_3 = next(rucksack_iter)
        identical_items = get_identical_items(group_1, group_2)
        total += get_rucksack_priority_sum(identical_items, group_3)
    return total


def get_rucksack_priority_sum(left, right):
    """
    Big O: O(n) / Time complexity: O(n)
    :param rucksack: A rucksack string that contains the items
    :return: Returns the total sum of the priority items in the rucksack

    """
    items = get_identical_items(left, right)
    left = list(set(left))
    right = list(set(right))

    sum = 0
    for char in items:
        priority = ord(char.lower()) - 96
        if char.isupper():
            priority += 26
        sum += priority
    return sum


def get_identical_items(left, right):
    """
    Big O: O(n) / Time complexity: O(n)
    :param left: A rucksack string that contains the items
    :param right: A rucksack string that contains the items
    :return: Returns the common priority items

    """
    left = list(set(left))
    right = list(set(right))

    items = []
    for char in left:
        if char in right:
            items.append(char)
    return "".join(items)

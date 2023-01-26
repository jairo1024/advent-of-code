def part1(rucksacks):
    """
    Big O: O(n^2) / Time complexity: O(n)
    :param rucksacks: A list of the rucksack strings
    :return: Returns the total sum of all of the priority items in all of the rucksacks
    """
    total = 0
    for rucksack in rucksacks:
        total += get_rucksack_priority_sum(rucksack)
    return total


def get_rucksack_priority_sum(rucksack):
    """
    Big O: O(n) / Time complexity: O(n)
    :param rucksack: A rucksack string that contains the items
    :return: Returns the total sum of the priority items in the rucksack

    """
    left = rucksack[: len(rucksack) // 2]
    left = list(set(left))
    right = rucksack[len(rucksack) // 2 :]
    right = list(set(right))

    sum = 0
    for char in left:
        if char in right:
            priority = ord(char.lower()) - 96
            if char.isupper():
                priority += 26
            sum += priority
    return sum

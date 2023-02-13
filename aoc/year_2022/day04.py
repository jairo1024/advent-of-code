def part1(ids):
    """
    Big O: O(n^2) / Time complexity: O(n)
    :param id: A list of the section pair strings
    :return: Returns the count of the assigned pairs that fully contain the other pair in each section
    """
    count = 0
    for id in ids:
        sections = get_sections(id)
        if sections[0].issubset(sections[1]) or sections[1].issubset(sections[0]):
            count = count + 1

    return count


def part2(ids):
    """
    Big O: O(n^2) / Time complexity: O(n^2)
    :param id: A list of the section pair strings
    :return: Returns the count of the assigned pairs that contain any of the other values in the other section
    """
    count = 0
    for id in ids:
        sections = get_sections(id)
        if bool(sections[0] & sections[1]):
            count = count + 1

    return count


def get_sections(id):
    """
    Big O: O(n) / Time complexity: O(n)
    :param id: A string of the assigned pair
    :return: Returns the range of the sections from the id
    """

    section_1, section_2 = id.split(",")
    return [get_range(section_1), get_range(section_2)]


def get_range(id):
    start, end = id.split("-")
    return set([x for x in range(int(start), int(end) + 1)])

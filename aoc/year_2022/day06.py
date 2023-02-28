def part1(datastream):
    """
    Big O: Time complexity: O(n^2) / Space complexity: O(n)
    :param datastream: A string of datastreams
    :return: Returns the index of the first start-of-packet marker

    Input:
        datastream: "bvwbjplbgvbhsrlpgdmjqwftvncz"

    Return:
        5
    """

    return find_marker(datastream, 4)


def find_marker(datastream, sequence_amount):
    """
    Big O: Time complexity: O(n^2) / Space complexity: O(n)
    :param datastream: A string of datastreams
    :param sequence_amount: The number of sequence of characters to look for
    :return: Returns the index of the first start-of-packet marker

    Input:
        datastream: "bvwbjplbgvbhsrlpgdmjqwftvncz"
        sequence_amount: 4

    Return:
        5
    """
    sequence = []
    for index, char in enumerate(datastream):
        if char in sequence:
            sequence = _remove_duplicate_sequence(char, sequence)
            sequence.append(char)
        else:
            sequence.append(char)
            if len(sequence) == sequence_amount:
                return index + 1


def _remove_duplicate_sequence(duplicated_char, sequence_list):
    for value in sequence_list[:]:
        if duplicated_char not in sequence_list:
            break
        sequence_list.pop(0)

    return sequence_list

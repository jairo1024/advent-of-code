from aoc.year_2022.day07.folder import Folder
from aoc.year_2022.day07.file import File
from more_itertools import peekable


def generate_tree(terminal_output):
    root_folder = None
    current_folder = None
    if terminal_output[0] == "$ cd /":
        root_folder = Folder("root")
        current_folder = root_folder
    else:
        raise Exception("Tree is not starting with root")

    cmds_iter = peekable(terminal_output[1:])
    for cmd in cmds_iter:
        if cmd.startswith("$ cd"):
            folder_name = cmd.split(" ")[2]
            if folder_name != "..":
                #                current_folder = [folder for folder in current_folder.get_folders() if folder.get_name() == folder_name][0]
                for folder in current_folder.get_folders():
                    if folder.get_name() == folder_name:
                        current_folder = folder
                        break
            else:
                parent = current_folder.get_parent()
                current_folder = parent

        elif cmd == "$ ls":
            while cmds_iter and not cmds_iter.peek().startswith("$"):
                next_content = next(cmds_iter)
                if next_content.startswith("dir"):
                    folder_name = next_content.split(" ")[1]
                    sub_folder = Folder(folder_name, current_folder)
                    current_folder.add_folder(sub_folder)

                else:
                    file = File(current_folder, next_content)
                    current_folder.add_file(file)

    return root_folder


# class File:
#    """
#    A data structure to convert a raw file input to an object that can be used with the Folder class.
#    """
#
#    def __init__(self, parent: 'Folder', raw_input: str):
#    """
#    Constructor of the File class.
#    :param parent: A Folder class object that the file is associated with
#    :param raw_input: The raw input from the Linux ls command of the file
#
#    Input:
#        parent (Folder Object): Folder("folder_name", "root")
#        raw_input (str): "100 a.txt"
#    """
#        parsed = raw_input.split(" ")
#        self.name = parsed[1]
#        self.size = int(parsed[0])
#        self.parent = parent
#
#    def get_name(self) -> str:
#    """
#    Getter method to return the name of the file.
#    :return (str): Returns the name of the file
#
#    Input:
#        None
#
#    Return:
#        "a.txt"
#    """
#        return self.name
#
#    def get_size(self) -> int:
#    """
#    Getter method to return the size of the file.
#    :return (int): Returns the size of the file
#
#    Input:
#        None
#
#    Return:
#        100
#    """
#        return self.size
#
#    def get_parent(self) -> 'Folder':
#    """
#    Getter method to return the parent Folder object.
#    :return (Folder Object): Returns the parent Folder object
#
#    Input:
#        None
#
#    Return:
#        Folder Object
#    """
#        return self.parent
#
# class Folder:
#
#    def __init__(self, name: str, parent: 'Folder'):
#        pass
#
# def part1(datastream):
#    """
#    Big O: Time complexity: O(n^2) / Space complexity: O(n)
#    :param datastream: A string of datastreams
#    :return: Returns the index of the first start-of-packet marker using a sequence of 4
#
#    Input:
#        datastream: "bvwbjplbgvbhsrlpgdmjqwftvncz"
#
#    Return:
#        5
#    """
#
#    return find_marker(datastream, 4)
#
#
# def part2(datastream):
#    """
#    Big O: Time complexity: O(n^2) / Space complexity: O(n)
#    :param datastream: A string of datastreams
#    :return: Returns the index of the first start-of-packet marker using a sequence of 14
#
#    Input:
#        datastream: "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
#
#    Return:
#        19
#    """
#
#    return find_marker(datastream, 14)
#
#
# def find_marker(datastream, sequence_amount):
#    """
#    Big O: Time complexity: O(n^2) / Space complexity: O(n)
#    :param datastream: A string of datastreams
#    :param sequence_amount: The number of sequence of characters to look for
#    :return: Returns the index of the first start-of-packet marker
#
#    Input:
#        datastream: "bvwbjplbgvbhsrlpgdmjqwftvncz"
#        sequence_amount: 4
#
#    Return:
#        5
#    """
#    sequence = []
#    for index, char in enumerate(datastream):
#        if char in sequence:
#            sequence = _remove_duplicate_sequence(char, sequence)
#            sequence.append(char)
#        else:
#            sequence.append(char)
#            if len(sequence) == sequence_amount:
#                return index + 1
#
#
# def _remove_duplicate_sequence(duplicated_char, sequence_list):
#    for value in sequence_list[:]:
#        if duplicated_char not in sequence_list:
#            break
#        sequence_list.pop(0)
#
#    return sequence_list

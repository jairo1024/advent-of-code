from aoc.year_2022.day07.folder import Folder


class File:
    """
    A data structure to convert a raw file input to an object that can be used with the Folder class.
    """

    def __init__(self, parent: "Folder", raw_input: str):
        """
        Constructor of the File class.
        :param parent: A Folder class object that the file is associated with
        :param raw_input: The raw input from the Linux ls command of the file

        Input:
            parent (Folder Object): Folder("folder_name", "root")
            raw_input (str): "100 a.txt"

        Return:
            None
        """
        parsed = raw_input.split(" ")
        self.name = parsed[1]
        self.size = int(parsed[0])
        self.parent = parent

    def get_name(self) -> str:
        """
        Getter method to return the name of the file.
        :return (str): Returns the name of the file

        Input:
            None

        Return:
            "a.txt"
        """
        return self.name

    def get_size(self) -> int:
        """
        Getter method to return the size of the file.
        :return (int): Returns the size of the file

        Input:
            None

        Return:
            100
        """
        return self.size

    def get_parent(self) -> "Folder":
        """
        Getter method to return the parent Folder object.
        :return (Folder Object): Returns the parent Folder object

        Input:
            None

        Return:
            Folder Object
        """
        return self.parent

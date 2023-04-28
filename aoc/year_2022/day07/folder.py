class Folder:
    """
    A data structure to track the information of a Folder.
    """

    def __init__(self, name: str, parent: "Folder" = None):
        """
        Constructor of the Folder class.
        :param name: The name of the folder
        :param parent: The parent Folder class object for this folder. Using no parent means this is the root Folder.

        Input:
            name (str): "my_folder_name"
            parent (Folder Object): Folder("folder_name", "root")

        Return:
            None
        """
        self.name = name
        self.parent = parent
        self.folders = []
        self.files = []

    def get_name(self) -> str:
        """
        Getter method to return the name of the folder.
        :return (str): Returns the name of the folder

        Input:
            None

        Return:
            "my_folder"
        """
        return self.name

    def is_root(self) -> bool:
        """
        A method to determine if this folder is the root directory or not.
        :return (boolean): Returns True/False if the folder is the root directory

        Input:
            None

        Return:
            True or False
        """
        if self.parent:
            return False
        else:
            return True

    def get_parent(self) -> "Folder":
        """
        A method that returns the parent of this Folder.
        :return (Folder): Returns the parent Folder object or None if it has no parent directory

        Input:
            None

        Return:
            Folder Object or None
        """
        return self.parent

    def add_folder(self, folder: "Folder"):
        """
        A method that adds a Folder object to this folder.

        Input:
            folder (Folder Object): Folder("folder_name")

        Return:
            None
        """
        self.folders.append(folder)

    def get_folders(self) -> list["Folder"]:
        """
        A method that returns the list of Folder objects in this Folder.
        :return (list): Returns the list of Folder objects of this Folder

        Input:
            None

        Return:
            A list of Folder Objects
        """
        return self.folders

    def add_file(self, file: "File"):
        """
        A method that adds a File object to this folder.

        Input:
            file (File Object): File(Folder("foo"), "100 a.txt")

        Return:
            None
        """
        self.files.append(file)

    def get_files(self) -> list["File"]:
        """
        A method that returns the list of File objects in this Folder.
        :return (list): Returns the list of File objects of this Folder

        Input:
            None

        Return:
            A list of File Objects
        """
        return self.files

    def get_folder_size(self) -> int:
        """
        A method that returns the total size of the Folder.
        :return (int): Returns the total size of the Folder in bytes

        Input:
            None

        Return:
            int
        """
        size = 0

        for file in self.files:
            size += file.get_size()

        for folder in self.folders:
            size += folder.get_folder_size()

        return size

    def is_empty(self) -> bool:
        """
        A method to determine if this folder is empty.
        :return (boolean): Returns True if the folder is empty

        Input:
            None

        Return:
            True or False
        """
        if self.folders or self.files:
            return False

        return True

    def print_tree(self):
        """
        A method to print the structure tree of the Folder.

        Input:
            None

        Return:
            None
        """
        print(self.__get_tree())

    def __get_tree(self, depth: str = 0) -> str:
        tree = ""

        if self.is_root():
            tree = (
                "     " * depth
                + f"{self.get_name()} - {self.get_folder_size()} bytes (Dir)\n"
            )
        else:
            tree = (
                "     " * (depth - 1)
                + f"|___ {self.get_name()} - {self.get_folder_size()} bytes (Dir)\n"
            )

        for file in self.files:
            tree += (
                "     " * depth
                + f"|___ {file.get_name()} - {file.get_size()} bytes (File)\n"
            )

        for folder in self.folders:
            tree += folder.__get_tree(depth + 1)

        return tree

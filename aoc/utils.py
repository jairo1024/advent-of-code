def readlines_from_file(path):
    """
    Will read the content of a file and return it as a list
    :param path: The path to the file to read the lines from
    :return: Returns a list of the content from the file
    """

    with open(path) as f:
        return f.read().splitlines()

from aoc.year_2022.day07.file import File
from aoc.year_2022.day07.folder import Folder
import pytest


class TestFolderClass:
    def test_folder_object_can_be_created(self):
        folder_name = "foo"

        my_folder = Folder(folder_name)

        assert isinstance(my_folder, Folder)

    class TestGetName:
        def test_name_is_returned(self):
            folder_name = "foo"
            parent_folder = Folder(folder_name)

            name = parent_folder.get_name()

            assert name == folder_name

    class TestIsRoot:
        def test_is_not_root_folder(self):
            folder_name = "foo"
            parent_folder = Folder("bar")

            my_folder = Folder(folder_name, parent_folder)

            assert not my_folder.is_root()

        def test_is_root_folder(self):
            folder_name = "foo"
            parent_folder = Folder("bar")

            my_folder = Folder(folder_name)

            assert my_folder.is_root()

    class TestGetParent:
        def test_parent_is_returned_for_a_non_root_folder(self):
            folder_name = "foo"
            parent_folder = Folder("bar")
            my_folder = Folder(folder_name, parent_folder)

            parent = my_folder.get_parent()

            assert parent == parent_folder

        def test_no_parent_is_returned_for_root_folder(self):
            folder_name = "foo"
            parent_folder = Folder("bar")
            my_folder = Folder(folder_name)

            parent = my_folder.get_parent()

            assert not parent

    class TestAddAndGetFolders:
        def test_a_folder_can_be_added(self):
            parent_folder = Folder("foo")
            sub_folder = Folder("bar", parent_folder)

            parent_folder.add_folder(sub_folder)
            folders = parent_folder.get_folders()

            assert folders == [sub_folder]

        def test_multiple_folders_can_be_added(self):
            parent_folder = Folder("foo")
            sub_folder_1 = Folder("bar_1", parent_folder)
            sub_folder_2 = Folder("bar_2", parent_folder)

            parent_folder.add_folder(sub_folder_1)
            parent_folder.add_folder(sub_folder_2)
            folders = parent_folder.get_folders()

            assert folders == [sub_folder_1, sub_folder_2]

    class TestAddAndGetFiles:
        def test_a_file_can_be_added(self):
            my_folder = Folder("foo")
            my_file = File(my_folder, "100 a.txt")

            my_folder.add_file(my_file)
            files = my_folder.get_files()

            assert files == [my_file]

        def test_multiple_files_can_be_added(self):
            my_folder = Folder("foo")
            file_1 = File(my_folder, "100 a.txt")
            file_2 = File(my_folder, "99 b.txt")

            my_folder.add_file(file_1)
            my_folder.add_file(file_2)
            files = my_folder.get_files()

            assert files == [file_1, file_2]

    class TestAddFilesAndFolders:
        def test_multiple_folders_and_files_can_be_added(self):
            parent_folder = Folder("foo")
            sub_folder_1 = Folder("bar_1", parent_folder)
            sub_folder_2 = Folder("bar_2", parent_folder)
            file_1 = File(parent_folder, "100 a.txt")
            file_2 = File(parent_folder, "99 b.txt")

            parent_folder.add_folder(sub_folder_1)
            parent_folder.add_folder(sub_folder_2)
            parent_folder.add_file(file_1)
            parent_folder.add_file(file_2)
            folders = parent_folder.get_folders()
            files = parent_folder.get_files()

            assert folders == [sub_folder_1, sub_folder_2]
            assert files == [file_1, file_2]

        def test_uneven_number_of_folders_and_files_can_be_added(self):
            parent_folder = Folder("foo")
            sub_folder_1 = Folder("bar_1", parent_folder)
            sub_folder_2 = Folder("bar_2", parent_folder)
            file_1 = File(parent_folder, "100 a.txt")

            parent_folder.add_folder(sub_folder_1)
            parent_folder.add_folder(sub_folder_2)
            parent_folder.add_file(file_1)
            folders = parent_folder.get_folders()
            files = parent_folder.get_files()

            assert folders == [sub_folder_1, sub_folder_2]
            assert files == [file_1]

    class TestGetFolderSize:
        def test_empty_folder(self):
            parent_folder = Folder("foo")

            size = parent_folder.get_folder_size()

            assert size == 0

        def test_a_file_can_be_counted(self):
            parent_folder = Folder("foo")
            file_1 = File(parent_folder, "100 a.txt")
            parent_folder.add_file(file_1)

            size = parent_folder.get_folder_size()

            assert size == 100

        def test_multiple_files_can_be_counted(self):
            parent_folder = Folder("foo")
            file_1 = File(parent_folder, "100 a.txt")
            file_2 = File(parent_folder, "50 b.txt")
            parent_folder.add_file(file_1)
            parent_folder.add_file(file_2)

            size = parent_folder.get_folder_size()

            assert size == 150

        def test_a_sub_folder_with_files_can_be_counted(self):
            parent_folder = Folder("foo")
            sub_folder_1 = Folder("bar", parent_folder)
            file_1 = File(sub_folder_1, "100 a.txt")
            file_2 = File(sub_folder_1, "50 b.txt")
            file_3 = File(sub_folder_1, "25 b.txt")
            parent_folder.add_folder(sub_folder_1)
            sub_folder_1.add_file(file_1)
            sub_folder_1.add_file(file_2)
            sub_folder_1.add_file(file_3)

            size = parent_folder.get_folder_size()

            assert size == 175

        def test_a_3_depth_sub_folder_with_files_can_be_counted(self):
            parent_folder = Folder("foo")
            sub_folder_1 = Folder("bar_1", parent_folder)
            sub_folder_2 = Folder("bar_2", sub_folder_1)
            sub_folder_3 = Folder("bar_3", sub_folder_2)
            file_1 = File(sub_folder_3, "100 a.txt")
            file_2 = File(sub_folder_3, "50 b.txt")
            file_3 = File(sub_folder_3, "25 b.txt")
            file_4 = File(sub_folder_3, "25 b.txt")
            parent_folder.add_folder(sub_folder_1)
            sub_folder_1.add_folder(sub_folder_2)
            sub_folder_2.add_folder(sub_folder_3)
            sub_folder_3.add_file(file_1)
            sub_folder_3.add_file(file_2)
            sub_folder_3.add_file(file_3)
            sub_folder_3.add_file(file_4)

            size = parent_folder.get_folder_size()

            assert size == 200

        def test_a_3_depth_sub_folder_with_files_in_each_folder_can_be_counted(self):
            parent_folder = Folder("foo")
            sub_folder_1 = Folder("bar_1", parent_folder)
            sub_folder_2 = Folder("bar_2", sub_folder_1)
            sub_folder_3 = Folder("bar_3", sub_folder_2)
            file_1 = File(parent_folder, "100 a.txt")
            file_2 = File(sub_folder_1, "50 b.txt")
            file_3 = File(sub_folder_2, "25 c.txt")
            file_4 = File(sub_folder_3, "25 d.txt")
            file_5 = File(sub_folder_3, "25 e.txt")
            parent_folder.add_folder(sub_folder_1)
            sub_folder_1.add_folder(sub_folder_2)
            sub_folder_2.add_folder(sub_folder_3)
            parent_folder.add_file(file_1)
            sub_folder_1.add_file(file_2)
            sub_folder_2.add_file(file_3)
            sub_folder_3.add_file(file_4)
            sub_folder_3.add_file(file_5)

            size = parent_folder.get_folder_size()

            assert size == 225

    class TestIsEmpty:
        def test_no_files_or_folders(self):
            parent_folder = Folder("foo")

            is_empty = parent_folder.is_empty()

            assert is_empty

        def test_contains_a_folder(self):
            parent_folder = Folder("foo")
            sub_folder_1 = Folder("bar_1", parent_folder)
            parent_folder.add_folder(sub_folder_1)

            is_empty = parent_folder.is_empty()

            assert not is_empty

        def test_contains_multiple_folders(self):
            parent_folder = Folder("foo")
            sub_folder_1 = Folder("bar_1", parent_folder)
            sub_folder_2 = Folder("bar_2", parent_folder)
            parent_folder.add_folder(sub_folder_1)
            parent_folder.add_folder(sub_folder_2)

            is_empty = parent_folder.is_empty()

            assert not is_empty

        def test_contains_a_file(self):
            parent_folder = Folder("foo")
            file_1 = File(parent_folder, "100 a.txt")
            parent_folder.add_file(file_1)

            is_empty = parent_folder.is_empty()

            assert not is_empty

        def test_contains_multiple_files(self):
            parent_folder = Folder("foo")
            file_1 = File(parent_folder, "100 a.txt")
            file_2 = File(parent_folder, "120 b.txt")
            parent_folder.add_file(file_1)
            parent_folder.add_file(file_2)

            is_empty = parent_folder.is_empty()

            assert not is_empty

        def test_contains_files_and_folders(self):
            parent_folder = Folder("foo")
            sub_folder_1 = Folder("bar_1", parent_folder)
            sub_folder_2 = Folder("bar_2", parent_folder)
            file_1 = File(parent_folder, "100 a.txt")
            file_2 = File(parent_folder, "120 b.txt")
            parent_folder.add_folder(sub_folder_1)
            parent_folder.add_folder(sub_folder_2)
            parent_folder.add_file(file_1)
            parent_folder.add_file(file_2)

            is_empty = parent_folder.is_empty()

            assert not is_empty

    class TestPrintTree:
        def test_empty_folder(self, capfd):
            expected_tree = "foo - 0 bytes (Dir)\n\n"
            parent_folder = Folder("foo")

            parent_folder.print_tree()
            printed_tree, err = capfd.readouterr()

            assert printed_tree == expected_tree

        def test_one_file_only(self, capfd):
            expected_tree = (
                "foo - 100 bytes (Dir)\n" "|___ a.txt - 100 bytes (File)\n\n"
            )
            parent_folder = Folder("foo")
            file_1 = File(parent_folder, "100 a.txt")
            parent_folder.add_file(file_1)

            parent_folder.print_tree()
            printed_tree, err = capfd.readouterr()

            assert printed_tree == expected_tree

        def test_one_empty_folder_only(self, capfd):
            expected_tree = "foo - 0 bytes (Dir)\n" "|___ bar - 0 bytes (Dir)\n\n"
            parent_folder = Folder("foo")
            sub_folder = Folder("bar", parent_folder)
            parent_folder.add_folder(sub_folder)

            parent_folder.print_tree()
            printed_tree, err = capfd.readouterr()

            assert printed_tree == expected_tree

        def test_one_file_and_one_empty_folder(self, capfd):
            expected_tree = (
                "foo - 100 bytes (Dir)\n"
                "|___ a.txt - 100 bytes (File)\n"
                "|___ bar - 0 bytes (Dir)\n\n"
            )
            parent_folder = Folder("foo")
            sub_folder = Folder("bar", parent_folder)
            file_1 = File(parent_folder, "100 a.txt")
            parent_folder.add_folder(sub_folder)
            parent_folder.add_file(file_1)

            parent_folder.print_tree()
            printed_tree, err = capfd.readouterr()

            assert printed_tree == expected_tree

        def test_multiple_files_and_multiple_empty_folders(self, capfd):
            expected_tree = (
                "foo - 290 bytes (Dir)\n"
                "|___ a.txt - 100 bytes (File)\n"
                "|___ hello.txt - 70 bytes (File)\n"
                "|___ world.txt - 120 bytes (File)\n"
                "|___ bar - 0 bytes (Dir)\n"
                "|___ foo - 0 bytes (Dir)\n\n"
            )
            parent_folder = Folder("foo")
            sub_folder_1 = Folder("bar", parent_folder)
            sub_folder_2 = Folder("foo", parent_folder)
            file_1 = File(parent_folder, "100 a.txt")
            file_2 = File(parent_folder, "70 hello.txt")
            file_3 = File(parent_folder, "120 world.txt")
            parent_folder.add_folder(sub_folder_1)
            parent_folder.add_folder(sub_folder_2)
            parent_folder.add_file(file_1)
            parent_folder.add_file(file_2)
            parent_folder.add_file(file_3)

            parent_folder.print_tree()
            printed_tree, err = capfd.readouterr()

            assert printed_tree == expected_tree

        def test_a_nested_sub_directory_depth_2(self, capfd):
            expected_tree = (
                "foo - 0 bytes (Dir)\n"
                "|___ bar - 0 bytes (Dir)\n"
                "     |___ other_folder - 0 bytes (Dir)\n\n"
            )
            parent_folder = Folder("foo")
            sub_folder_1 = Folder("bar", parent_folder)
            sub_folder_2 = Folder("other_folder", sub_folder_1)
            sub_folder_1.add_folder(sub_folder_2)
            parent_folder.add_folder(sub_folder_1)

            parent_folder.print_tree()
            printed_tree, err = capfd.readouterr()

            assert printed_tree == expected_tree

        def test_a_nested_sub_directory_depth_3_with_files(self, capfd):
            expected_tree = (
                "foo - 30 bytes (Dir)\n"
                "|___ a.txt - 5 bytes (File)\n"
                "|___ bar - 25 bytes (Dir)\n"
                "     |___ b.txt - 10 bytes (File)\n"
                "     |___ other_folder_1 - 15 bytes (Dir)\n"
                "          |___ other_folder_2 - 15 bytes (Dir)\n"
                "               |___ c.txt - 15 bytes (File)\n\n"
            )
            parent_folder = Folder("foo")
            bar_folder = Folder("bar", parent_folder)
            sub_folder_1 = Folder("other_folder_1", bar_folder)
            sub_folder_2 = Folder("other_folder_2", sub_folder_1)
            parent_folder.add_folder(bar_folder)
            bar_folder.add_folder(sub_folder_1)
            sub_folder_1.add_folder(sub_folder_2)
            file_1 = File(parent_folder, "5 a.txt")
            file_2 = File(bar_folder, "10 b.txt")
            file_3 = File(sub_folder_2, "15 c.txt")
            parent_folder.add_file(file_1)
            bar_folder.add_file(file_2)
            sub_folder_2.add_file(file_3)

            parent_folder.print_tree()
            printed_tree, err = capfd.readouterr()

            assert printed_tree == expected_tree

        def test_multiple_nested_sub_directory_depth_3_with_files(self, capfd):
            expected_tree = (
                "foo - 90 bytes (Dir)\n"
                "|___ a.txt - 5 bytes (File)\n"
                "|___ bar - 25 bytes (Dir)\n"
                "     |___ b.txt - 10 bytes (File)\n"
                "     |___ other_folder_1 - 15 bytes (Dir)\n"
                "          |___ other_folder_2 - 15 bytes (Dir)\n"
                "               |___ c.txt - 15 bytes (File)\n"
                "|___ bar_bar - 60 bytes (Dir)\n"
                "     |___ d.txt - 20 bytes (File)\n"
                "     |___ other_folder_3 - 40 bytes (Dir)\n"
                "          |___ other_folder_4 - 40 bytes (Dir)\n"
                "               |___ e.txt - 40 bytes (File)\n\n"
            )
            parent_folder = Folder("foo")
            bar_folder = Folder("bar", parent_folder)
            bar_bar_folder = Folder("bar_bar", parent_folder)
            sub_folder_1 = Folder("other_folder_1", bar_folder)
            sub_folder_2 = Folder("other_folder_2", sub_folder_1)
            sub_folder_3 = Folder("other_folder_3", bar_bar_folder)
            sub_folder_4 = Folder("other_folder_4", sub_folder_3)
            parent_folder.add_folder(bar_folder)
            parent_folder.add_folder(bar_bar_folder)
            bar_folder.add_folder(sub_folder_1)
            sub_folder_1.add_folder(sub_folder_2)
            bar_bar_folder.add_folder(sub_folder_3)
            sub_folder_3.add_folder(sub_folder_4)
            file_1 = File(parent_folder, "5 a.txt")
            file_2 = File(bar_folder, "10 b.txt")
            file_3 = File(sub_folder_2, "15 c.txt")
            file_4 = File(bar_bar_folder, "20 d.txt")
            file_5 = File(sub_folder_4, "40 e.txt")
            parent_folder.add_file(file_1)
            bar_folder.add_file(file_2)
            sub_folder_2.add_file(file_3)
            bar_bar_folder.add_file(file_4)
            sub_folder_4.add_file(file_5)

            parent_folder.print_tree()
            printed_tree, err = capfd.readouterr()

            assert printed_tree == expected_tree

        def test_provided_example(self, capfd):
            expected_tree = (
                "root - 48381165 bytes (Dir)\n"
                "|___ b.txt - 14848514 bytes (File)\n"
                "|___ c.dat - 8504156 bytes (File)\n"
                "|___ a - 94853 bytes (Dir)\n"
                "     |___ f - 29116 bytes (File)\n"
                "     |___ g - 2557 bytes (File)\n"
                "     |___ h.lst - 62596 bytes (File)\n"
                "     |___ e - 584 bytes (Dir)\n"
                "          |___ i - 584 bytes (File)\n"
                "|___ d - 24933642 bytes (Dir)\n"
                "     |___ j - 4060174 bytes (File)\n"
                "     |___ d.log - 8033020 bytes (File)\n"
                "     |___ d.ext - 5626152 bytes (File)\n"
                "     |___ k - 7214296 bytes (File)\n\n"
            )
            root_folder = Folder("root")
            a_folder = Folder("a", root_folder)
            e_folder = Folder("e", a_folder)
            d_folder = Folder("d", root_folder)

            root_file_1 = File(root_folder, "14848514 b.txt")
            root_file_2 = File(root_folder, "8504156 c.dat")
            a_file_1 = File(a_folder, "29116 f")
            a_file_2 = File(a_folder, "2557 g")
            a_file_3 = File(a_folder, "62596 h.lst")
            e_file_1 = File(e_folder, "584 i")
            d_file_1 = File(d_folder, "4060174 j")
            d_file_2 = File(d_folder, "8033020 d.log")
            d_file_3 = File(d_folder, "5626152 d.ext")
            d_file_4 = File(d_folder, "7214296 k")

            root_folder.add_file(root_file_1)
            root_folder.add_file(root_file_2)
            a_folder.add_file(a_file_1)
            a_folder.add_file(a_file_2)
            a_folder.add_file(a_file_3)
            e_folder.add_file(e_file_1)
            d_folder.add_file(d_file_1)
            d_folder.add_file(d_file_2)
            d_folder.add_file(d_file_3)
            d_folder.add_file(d_file_4)

            root_folder.add_folder(a_folder)
            root_folder.add_folder(d_folder)
            a_folder.add_folder(e_folder)

            root_folder.print_tree()
            printed_tree, err = capfd.readouterr()

            assert printed_tree == expected_tree

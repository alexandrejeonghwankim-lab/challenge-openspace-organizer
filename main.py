from utils.table import Table
from utils.openspace import OpenSpace
from utils.file_utils import read_namelist_file


# under is for the test

def main():
    names = read_namelist_file("new_colleagues.txt")
    space = OpenSpace()
    space.organize(names)
    space.display()
    space.store("new_list.txt")

if __name__ == "__main__":
    main()

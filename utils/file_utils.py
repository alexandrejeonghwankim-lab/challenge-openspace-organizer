def read_namelist_file(filename):
    """
    This function will open a file and read the contents of file.
    It opens the file, reads its contents as string, 
    and then splits the contents into a list of names using the newline ("\n").

    Finally it returns the list of names.
    
    """
    with open(filename, "r") as file:
        content = file.read()
        names = content.split("\n")
    return names


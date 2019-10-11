"""
Collected functions
"""

filename = "inv.data"
def read_inv():
    """
    reads file
    """
    f = open(filename, "r")
    return f.read()


def write_to_file(content, mode):
    """
    writes to file
    """
    with open(filename, mode) as filehandle:
        filehandle.write(content.strip() + "\n")


def replace_content(item):
    """
    replaces content in file
    """
    content = read_inv()
    if item in content:
        modified_content = content.replace(item, "")
        write_to_file(modified_content, "w")
        print("Item was dropped")
    else:
        return print("there's no " + str(item) + " in bag")
    return read_inv()

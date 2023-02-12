import re
import os
from placeObj import Macro


def read_BookShelf(dir, name):
    path = os.path.join(dir, name)
    for file in os.listdir(path):
        # read .aux
        if file == name + ".aux":
            with open(os.path.join(path, file), 'r') as f:
                for line in f:
                    line = line.strip() # remove newline
                    file_regex = r"([^\s]+\.nodes|[^\s]+\.nets|[^\s]+\.wts|[^\s]+\.pl|[^\s]+\.scl)"
                    bkshelf_files = re.findall(file_regex, line)
                    assert len(bkshelf_files) == 5
        # read .nodes
        if file == name + ".nodes":
            with open(os.path.join(path, file), 'r') as f:
                for line in f:
                    line = line.strip() # remove newline
                    node_regex = r"\s*(o\d+)\t(\d+)\t(\d+)(?:\t(\S+))?"
                    node_info = re.split(node_regex, line)
                    if len(node_info) >= 6:
                        # macro
                        if node_info[4] == "terminal":
                            module_name = node_info[1]
                            module_height = float(node_info[2])
                            module_width = float(node_info[3])
                            macro = Macro(name=module_name,
                                        height=module_height, 
                                        width=module_width)
                            # macro.dump()

        # read .pl
        if file == name + ".pl":
            with open(os.path.join(path, file), 'r') as f:
                for line in f:
                    line = line.strip() # remove newline
                    node_regex = r"\s*(o\d+)\t(\d+)\t(\d+)\t:\s*([^\s]*\w[^\s]*)"
                    node_info = re.split(node_regex, line)
                    if len(node_info) >= 6:
                        # need to build a class structure to feed in macro xy/direction
                        pass

        # read .nets
        # read .wts
        # read .scl
read_BookShelf("../benchmark/ispd2005", "adaptec1")


def plc_to_img():
    pass


def img_to_plc():
    pass

import os
import xml.etree.ElementTree as et

from table import Table
coords = [
    [(5,28),(8,28),(11,28),(14,28),(17,28),(20,28),(23,28),(26,28),(29,28)],
    [(5,21),(8,21),(11,21),(14,21),(17,21),(20,21),(23,21),(26,21),(29,21)],
    [(5,15),(8,15),(11,15),(14,15),(17,15),(20,15),(23,15),(26,15),(29,15)]]



class Data:
    def __init__(self):
        name_xml = "tables.xml"
        folder_xml = "data"
        path = os.path.dirname(__file__)
        self.path_xml = os.path.join(path, folder_xml, name_xml)
        self.coords = coords

    def get_table(self, id):
        tree = et.parse(self.path_xml)
        root = tree.getroot()
        for element in root:
            if str(id) == element.attrib["id"]:
                return Table(int(id), element.text)

    def get_coords(self, x, y):
        return self.coords[y][x]

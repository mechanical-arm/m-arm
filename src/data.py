import os
import xml.etree.ElementTree as et

from table import Table
coords = [
    [(4,27),(7,28),(10,28),(13,28),(16,28),(19,28),(22,28),(25,28),(26,27)],
    [(4,20),(7,21),(10,21),(13,21),(16,21),(19,21),(21,21),(24,21),(26,20)],
    [(4,16),(7,16),(10,15),(13,15),(16,15),(19,15),(21,15),(24,15),(26,15)]
]
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

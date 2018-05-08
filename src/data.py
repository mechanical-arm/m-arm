import os
import xml.etree.ElementTree as et

from table import Table

class Data:
    def __init__(self):
        name_xml = "tables.xml"
        folder_xml = "data"
        path = os.path.dirname(__file__)
        self.path_xml = os.path.join(path, folder_xml, name_xml)
        print(self.get_table("4"))

    def get_table(self, id):
        tree = et.parse(self.path_xml)
        root = tree.getroot()
        for element in root:
            if id == element.attrib["id"]:
                return Table(id, element.text)

d = Data()

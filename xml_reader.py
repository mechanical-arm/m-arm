import xml.etree.ElementTree as et

class Table:
    def __init__(self, element):
        self.id = element.attrib["id"]
        self.nums = element.text.strip().split()

    def __str__(self):
        return self.id + " - " + str(self.nums)

class Reader:
    def __init__(self):
        self.tree = et.parse("tables.xml")
        self.root = self.tree.getroot()
        self.tables = dict()
        for element in self.root:
            new_table = Table(element)
            self.tables[new_table.id] = new_table

if __file__ == "__main__":
    r = Reader()
    for t in r.tables:
        print(r.tables[t])

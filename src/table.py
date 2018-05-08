
class Table:
    def __init__(self, id, text):
        self.matrix = self.parse(text)



    def parse(self, text):
        # remove tab
        try: text = text.translate(None, '\t')
        except: text = text.translate('\t')
        # split line
        text = text.split("\n")
        # split cell
        for p,line in enumerate(text):
            text[p] = line.split()
        return text[1:-1]

    def __str__(self):
        text = str()
        for line in self.matrix:
            for cell in line:
                text += cell + "\t"
            text += "\n"
        return text

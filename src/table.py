
class Table:
    def __init__(self, id, text):
        self.id = id
        self.matrix = self.parse(text)

    def parse(self, text):
        # remove tab
        try: text = text.translate(None, '\t')
        except: text = text.translate('\t')
        # split line
        text = text.split("\n")
        # split cell
        for p,line in enumerate(text):
            text[p] = list(map(int,line.split()))
        matrix = list()
        for line in text[1:-1]:
            row = list()
            for cell in line:
                row.append([cell,False])
            matrix.append([row,False])
        return matrix

    def call_num(self, num):
        for y,(line,l) in enumerate(self.matrix):
            for x,(cell,b) in enumerate (line):
                if num == cell:
                    line[x][1] = True
                    return (x,y)


    def row_bool(self, n_row):
        row = self.matrix[n_row][0]
        bool_sum = 0
        for num,bool in row:
            bool_sum += int(bool)
        return bool_sum

    def __str__(self):
        text = "ID: %s\n\n" % self.id
        for line,l in self.matrix:
            for cell in line:
                if cell == 0: cell = ""
                text += str(cell) + "\t"
            text += "\n"
        return text

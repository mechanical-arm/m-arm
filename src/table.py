
class Table:
    def __init__(self, id, text):
        self.id = id
        self.matrix = self.parse(text)
        self.last_prize = 1

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
                    return (x,y), self.control()

    def control(self):
        for n in range(3):
            if self.get_prize(n):
                self.add_prize()
                self.matrix[n][1] = not self.matrix[n][1]
                return self.last_prize * self.matrix[n][1]

    def add_prize(self):
        self.last_prize += 1

    def get_prize(self, n_row):
        prize = self.row_bool(n_row)
        if prize > self.last_prize:
            return prize

    def state(self):
        print("Last prize %d" %self.last_prize)
        for n in range(3): print(self.row_bool(n))

    def row_bool(self, n_row):
        row,state = self.matrix[n_row]
        if state: return False
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

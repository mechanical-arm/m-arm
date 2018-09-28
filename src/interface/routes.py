from flask import render_template, request
from interface import app

def bool_t(str):
    if str == "True":
        return True
    else: return False

def int_t(str):
    if str == "0":
        return " "
    else: return str

def get_table():
    import os
    path = os.path.dirname(__file__)
    path_table = os.path.join(path,"table")
    file = open(path_table, "r")
    table = list()
    for row in file:
        r = list()
        row = row.strip()
        cells = row.split()
        for cell in cells:
            c,b = cell.split("-")
            r.append([int_t(c),bool_t(b)])
        table.append(r)
    return table

print(get_table())

@app.route("/")

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home',table=get_table())

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name)

# Conexión a la base de datos SQLite
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Creación de tablas (si no existen)
c.execute('''CREATE TABLE IF NOT EXISTS table1
             (id INTEGER PRIMARY KEY, cell1_link TEXT, cell2_link TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS table2
             (id INTEGER PRIMARY KEY, cell1_link TEXT, cell2_link TEXT)''')

# Guardar los cambios en la base de datos y cerrar la conexión
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table1')
def table1():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT cell1_link, cell2_link FROM table1')
    elements = c.fetchall()
    conn.close()
    return render_template('tables/table1.html', elements=elements)

@app.route('/table2')
def table2():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT cell1_link, cell2_link FROM table2')
    elements = c.fetchall()
    conn.close()
    return render_template('tables/table2.html', elements=elements)

@app.route('/table1/save_link', methods=['POST'])
def save_link_table1():
    link = request.form['link']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO table1 (cell1_link) VALUES (?)', (link,))
    conn.commit()
    conn.close()
    return redirect('/table1')

@app.route('/table2/save_link', methods=['POST'])
def save_link_table2():
    link = request.form['link']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO table2 (cell1_link) VALUES (?)', (link,))
    conn.commit()
    conn.close()
    return redirect('/table2')

if __name__ == '__main__':
    app.run()
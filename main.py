import sqlite3 as sql
from flask import Flask, request, render_template

app = Flask(__name__)


def get_db_connection():
    conn = sql.connect('database.db')
    conn.row_factory = sql.Row
    return conn


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/comment', methods=['POST', 'GET'])
def commentMenu():
    if request.method == 'POST':
        try:
            name = request.form['name']
            comment = request.form['comment']

            with get_db_connection() as con:
                con.execute('INSERT INTO visitors (name, comment) VALUES (?, ?)', (name, comment))
                con.commit()
                msg = name + " your response has been noted"

        except:
            con.rollback()
            msg = "Oops! seems like an error occurred"

        finally:
            return render_template('comment.html', msg=msg)
    else:
        return render_template('comment.html')


@app.route('/view_comments', methods=['GET', 'POST'])
def view_comments():
    conn = get_db_connection()
    visitors = conn.execute('SELECT * FROM visitors').fetchall()
    conn.close()
    return render_template('view_comments.html', visitors=visitors)


@app.route('/progress')
def progressMenu():
    return render_template('progress.html')


@app.route('/contact')
def contactMenu():
    return render_template('contact.html')


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM visitors WHERE id = ?', (id,))
    conn.commit()
    visitors = conn.execute('SELECT * FROM visitors').fetchall()
    conn.close()
    msg = "Successfully Deleted!"
    return render_template('view_comments.html', msg=msg, visitors=visitors)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'fishHEAD':
            conn = get_db_connection()
            visitors = conn.execute('SELECT * FROM visitors').fetchall()
            conn.close()
            return render_template('view_comments.html', visitors=visitors)
        else:
            msg = 'Please input correct password'
            return render_template('admin.html', msg=msg)
    else:
        return render_template('admin.html')


if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

@app.route('/')
def index():
    data = db.read(None)

    return render_template('index.html', data = data)

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addBook', methods = ['POST', 'GET'])
def addBook():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new Book has been added")
        else:
            flash("A new Book can not be added")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updateBook', methods = ['POST'])
def updateBook():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('A Book has been updated')

        else:
            flash('The Book can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deleteBook', methods = ['POST'])
def deleteBook():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('The Book has been deleted')

        else:
            flash('The Book can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")

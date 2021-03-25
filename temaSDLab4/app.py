from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort

def get_db_connection():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite3.Row
	return conn

def get_cheltuiala(cheltuiala_id):
	conn = get_db_connection()
	cheltuiala = conn.execute('SELECT * FROM familie WHERE id = ?', (cheltuiala_id,)).fetchone()
	conn.close()
	if cheltuiala is None:
		abort(404)
	return cheltuiala

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

@app.route('/')
def index():
	conn = get_db_connection()
	cheltuieli = conn.execute('SELECT * FROM familie').fetchall()
	conn.close()
	return render_template('index.html', cheltuieli=cheltuieli)

@app.route('/<int:cheltuiala_id>')
def cheltuiala(cheltuiala_id):
	cheltuiala = get_cheltuiala(cheltuiala_id)
	return render_template('cheltuiala.html', cheltuiala=cheltuiala)

@app.route('/create', methods=('GET', 'POST'))
def create():
	if request.method == 'POST':
		valoare = request.form['valoare']
		detalii = request.form['detalii']

		if not valoare:
			flash('Introduceti o valoare!')
		else:
			conn = get_db_connection()
			conn.execute('INSERT INTO familie (valoare, detalii) VALUES (?,?)', (valoare, detalii))
			conn.commit()
			conn.close()
			return redirect(url_for('index'))
	return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
	cheltuiala = get_cheltuiala(id)

	if request.method == 'POST':
		valoare = request.form['valoare']
		detalii = request.form['detalii']

		if not valoare:
			flash('Valoarea nu a fost primita!')
		else:
			conn = get_db_connection()
			conn.execute('UPDATE familie SET valoare = ?, detalii = ? WHERE id = ?', (valoare, detalii, id))
			conn.commit()
			conn.close()
			return redirect(url_for('index'))
	return render_template('edit.html', cheltuiala=cheltuiala)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
	cheltuiala = get_cheltuiala(id)
	conn = get_db_connection()
	conn.execute('DELETE FROM familie WHERE id = ?', (id,))
	conn.commit()
	conn.close()
	return redirect(url_for('index'))

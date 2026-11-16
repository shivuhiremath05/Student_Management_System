from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from datetime import datetime
import json

app = Flask(__name__)
DATABASE = 'db.sqlite'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    db.executescript('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            usn TEXT UNIQUE NOT NULL,
            semester INTEGER NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            parent_name TEXT NOT NULL,
            parent_phone TEXT NOT NULL,
            parent_email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    db.commit()
    db.close()

@app.route('/')
def home():
    db = get_db()
    students = db.execute('SELECT * FROM students ORDER BY created_at DESC').fetchall()
    db.close()
    total_students = len(students)
    return render_template('home.html', students=students, total_students=total_students)

@app.route('/students/add/', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        try:
            db = get_db()
            db.execute('''
                INSERT INTO students (name, usn, semester, email, phone, address, parent_name, parent_phone, parent_email)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                request.form['name'],
                request.form['usn'],
                request.form['semester'],
                request.form['email'],
                request.form['phone'],
                request.form['address'],
                request.form['parent_name'],
                request.form['parent_phone'],
                request.form.get('parent_email', '')
            ))
            db.commit()
            db.close()
            return redirect(url_for('home'))
        except sqlite3.IntegrityError:
            return render_template('add_students.html', error='USN already exists!')
    return render_template('add_students.html')

@app.route('/students/edit/<int:id>/', methods=['GET', 'POST'])
def edit_student(id):
    db = get_db()
    student = db.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    
    if request.method == 'POST':
        db.execute('''
            UPDATE students 
            SET name=?, usn=?, semester=?, email=?, phone=?, address=?, parent_name=?, parent_phone=?, parent_email=?
            WHERE id=?
        ''', (
            request.form['name'],
            request.form['usn'],
            request.form['semester'],
            request.form['email'],
            request.form['phone'],
            request.form['address'],
            request.form['parent_name'],
            request.form['parent_phone'],
            request.form.get('parent_email', ''),
            id
        ))
        db.commit()
        db.close()
        return redirect(url_for('home'))
    
    db.close()
    return render_template('edit_students.html', student=student)

@app.route('/students/delete/<int:id>/')
def delete_student(id):
    db = get_db()
    db.execute('DELETE FROM students WHERE id = ?', (id,))
    db.commit()
    db.close()
    return redirect(url_for('home'))

@app.route('/students/details/<int:id>/')
def student_details(id):
    db = get_db()
    student = db.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    db.close()
    return render_template('details.html', student=student)

@app.route('/students/dashboard/')
def dashboard():
    db = get_db()
    total_students = db.execute('SELECT COUNT(*) FROM students').fetchone()[0]
    semester_data = db.execute('SELECT semester, COUNT(*) as count FROM students GROUP BY semester').fetchall()
    
    # Prepare data for charts
    semesters = [row['semester'] for row in semester_data]
    counts = [row['count'] for row in semester_data]
    
    db.close()
    return render_template('dashboard.html', total_students=total_students, semesters=json.dumps(semesters), counts=json.dumps(counts))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",  # set your MySQL password
    database="unimategame"
)
cursor = db.cursor(dictionary=True)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Register student
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        interests = request.form['interests']
        cursor.execute("INSERT INTO students (name, email, interests) VALUES (%s, %s, %s)",
                       (name, email, interests))
        db.commit()
        return redirect('/matches')
    return render_template('register.html')

# Show matches based on common interests
@app.route('/matches')
def matches():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('matches.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)

import sqlite3 
from flask import Flask, redirect, url_for, render_template, request, session

def register_user_to_db(username, email, password):
     conn = sqlite3.connect('database.db')
     cur = conn.cursor()
     cur.execute('INSERT INTO users(username, email, password) values (?,?,?)', (username, email, password))
     conn.commit()
     conn.close()

def check_user(username, email, password):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('Select username, email, password FROM users WHERE username=? and email=? and password=?', (username, email, password))
    
    result = cur.fetchone()
    if result:
        return True
    else:
        return False

app = Flask(__name__)
app.secret_key = 'BookCafe@tesdagyaf'

@app.route("/")
@app.route("/login.html")
def index():
    return render_template('login.html')

@app.route('/register.html', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        register_user_to_db(username, email, password)
        return redirect(url_for('index'))
    
    else:
        return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
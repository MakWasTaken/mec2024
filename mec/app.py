from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure value

# In-memory storage for prototype
users = {'user1': {'password': 'pass1', 'role': 'patient'},
         'user2': {'password': 'pass2', 'role': 'doctor'}}

# Initial registration
def register_user(username, password, role='patient'):
    if username not in users:
        users[username] = {'password': password, 'role': role}
        return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            flash('Login successful', 'success')
            return redirect(url_for('dashboard'))

        flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if register_user(username, password):
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))

        flash('Username already exists. Please choose another.', 'error')

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/wipe_data')
def wipe_data():
    global users
    users = {}
    flash('All registered accounts have been wiped.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

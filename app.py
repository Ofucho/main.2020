from flask import Flask,render_template, redirect, url_for, request
app = Flask(__name__)





@app.route('/login', methods=['GET', 'POST'])
def login_page():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != '1234':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():


    return render_template('dashboard.html')


















if __name__ == '__main__':
    app.run()

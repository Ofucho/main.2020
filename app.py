from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

import psycopg2
import pygal


@app.route('/login', methods=['POST', 'GET'])
def login_page():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != '1234':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('dashboard'))
    return render_template('login.html', error=error)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        return redirect(url_for('login_page'))

    return render_template('dashboard.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':

     return redirect(url_for('login_page'))


if __name__ == '__main__':
    app.run()

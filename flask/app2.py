from flask import Flask, session, render_template, request, redirect, g, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pyodbc
from flask_session import Session

user0 = Flask(__name__)
user0.secret_key = os.urandom(24)
user0.config["SESSION_PERMANENT"] = False
user0.config["SESSION_TYPE"] = "filesystem"


def connection():
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-4GHBHUH;'
                      'Database=QuickKartDB;'
                      'Trusted_Connection=yes;')
    return conn

# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=DESKTOP-4GHBHUH;'
#                       'Database=QuickKartDB;'
#                       'Trusted_Connection=yes;')
# cursor = conn.cursor()

# cursor = conn.cursor()
# cursor.execute('SELECT * FROM Users where RoleId = 2')
# for row in cursor:
#     print(row)
    
# cursor.close()
# conn.close()

@user0.route("/")
def main():
    # users = []
    # conn = connection()
    # cursur = conn.cursor()
    # cursur.execute('SELECT * FROM Users where RoleId = 2')
    # for row in cursur.fetchall():
    #     users.append({"Email":row[0], "Role_id": row[2], "Gender": row[3], "DOB": row[4], "Address": row[5]})
    # conn.close()
    # return render_template("login.html", users=users)
    return render_template('base.html')
global logged_user
# http://localhost:5000/pythonlogin/ - the following will be our login page, which will use both GET and POST requests
# @user.route("/login/", methods=['GET', 'POST'])
# def login():
#     # Output message if something goes wrong...
#     error_msg = ''
#     action = render_template('login.html', msg='')
#     if request.method == 'POST':
#         Session.pop('user', None)
#         if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#             username = request.form['username']
#             password = request.form['password']
#             logged_user = username
#             #Check if account exists  using MSSql
#             conn = connection()
#             cursur = conn.cursor()
#             cursur.execute('SELECT * FROM Users WHERE EmailId = ? AND UserPassword = ?', (username, password))
#             #Fetch one record and return result
#             account = cursur.fetchone()
#             if account:
#                 # Create session data, we can access this data in other routes
#                 # Redirect to home page
#                 # Session['username'] = account['username']
#                 action = render_template('landing.html', username = username)
#                 # msg1 = "Hello {0}".format(username)
#                 return action
#             else:
#                 #Account doent exist or username/password incorrect
#                 error_msg = 'Incorrect username/password!'
#                 action = render_template('login.html', error_msg = error_msg)

#         return action

@user0.route("/login/", methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    error_msg = ''
    action = render_template('login.html', msg='')
    if request.method == 'POST':
        session.pop('user', None)
        username = request.form['username']
        password = request.form['password']
        logged_user = username
        conn = connection()
        cursur = conn.cursor()
        cursur.execute('SELECT * FROM Users WHERE EmailId = ? AND UserPassword = ?', (username, password))
        #Fetch one record and return result
        account = cursur.fetchone()
        if account:
            session['user'] = request.form['username']
            return redirect(url_for('landing1'))
        else:
            #Account doent exist or username/password incorrect
            error_msg = 'Incorrect username/password!'
            action = render_template('login.html', error_msg = error_msg)
    return action


@user0.route("/landing/", methods=['GET', 'POST'])
def landing1():
    if g.user:
        return render_template('landing.html', user = session['user'])
    return redirect(url_for('login'))

@user0.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
        


@user0.route("/contact/")
def contact():
    return render_template('contact.html')
    
if __name__ == "__main__":
    user0.run(debug=True, port=5001)

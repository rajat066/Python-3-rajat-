from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pyodbc
from requests import session

user = Flask(__name__)


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

@user.route("/")
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
# http://localhost:5000/pythonlogin/ - the following will be our login page, which will use both GET and POST requests
@user.route("/login/", methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    error_msg = 'Something went wrong'
    action = render_template('login.html', msg='')
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        #Check if account exists  using MSSql
        conn = connection()
        cursur = conn.cursor()
        cursur.execute('SELECT * FROM Users WHERE EmailId = ? AND UserPassword = ?', (username, password))
        #Fetch one record and return result
        account = cursur.fetchone()
        if account:
            # Create session data, we can access this data in other routes
            # session['loggedin'] = True
            # session['id'] = account['id']
            # session['username'] = account['username']
            # Redirect to home page
            action = redirect("/landing")
            # msg1 = "Hello {0}".format(username)
            return action
        else:
            #Account doent exist or username/password incorrect
            msg = 'Incorrect username/password!'

    return action

@user.route("/landing/", methods=['GET', 'POST'])
def landing1():
    s


@user.route("/contact/")
def contact():
    return render_template('contact.html')
    
if __name__ == "__main__":
    user.run(debug=True, port=5001)

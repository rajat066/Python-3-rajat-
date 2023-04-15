from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pyodbc

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
    msg = 'Something went wrong'
    return render_template('login.html', msg='')

@user.route("/contact/")
def contact():
    return render_template('contact.html')
    
if __name__ == "__main__":
    user.run(debug=True, port=5001)
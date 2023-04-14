from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-4GHBHUH;'
                      'Database=QuickKartDB;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Users where RoleId = 2')
for row in cursor:
    print(row)
    
cursor.close()
conn.close()
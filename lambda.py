import sys

import csv

import sqlite3

import os

import pyodbc 



def handler(event, context):

    db_file = "nyc_medium.db"

    conn = sqlite3.connect(db_file)

    cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for SQLite};Direct=True;Database=nyc_medium.db;String Types= Unicode')

    cursor = cnxn.cursor()
    cursor.execute("SELECT Airline FROM flights where Dest='DEN'")
    res = c.fetchall()
    print(res)

    c = conn.cursor()

    ans = c.execute("SELECT Airline FROM flights where Dest='DEN'")

    ans = c.fetchall()

    conn.commit()

    conn.close()

    return ans

import random
import os
import sqlite3
import json

from time import strftime
from bottle import route, run, template, get, post, redirect, request, TEMPLATE_PATH, static_file

import markov

TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))

poem = None

def db_connect():
    db = sqlite3.connect('poems.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Poems
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             poem text,
             written_date timestamp)''')
    return c

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/cameron/Projects/python_poetry_generator/static')

@get('/')
def page():
    print poem
    return template('mainPage', poem=poem)


@post('/')
def enter_score():
    now = strftime("%Y-%m-%d %H:%M:%S")
    poem = markov.write(request.forms)
    global poem
    redirect('/')
    # db = sqlite3.connect('poems.db')
    # c = db.cursor()
    
    # c.execute('''INSERT INTO Poems (poem, written_date)
    #              VALUES (?, ?, ?)''', (data['poem'], now))
    # db.commit()
    # db.close()

@get('/poetry')
def scores_view():
    c = db_connect()
    c.execute('SELECT poem FROM Poems order by written_date DESC')
    data = c.fetchall()
    c.close()

    return template('poetry', data=data)


run(host='localhost', port=8080, debug=True)


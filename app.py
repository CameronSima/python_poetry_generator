import random
import os
import sqlite3
import json

from time import strftime
from bottle import route, run, template, get, post, redirect, request, TEMPLATE_PATH, static_file

import markov

TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))

DEBUG = False

if DEBUG:
    URL_PREFIX = ''
    STATIC_ROOT = '/home/cameron/Projects/python_poetry_generator/static'
else:
    URL_PREFIX = '/poetry_generator'
    STATIC_ROOT = '/home/cameron/python_poetry_generator/static'

poem = None

def db_connect():
    db = sqlite3.connect('poems.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Poems
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             poem text,
             written_date timestamp)''')
    return c

@route(URL_PREFIX + '/static/<filename>')
def server_static(filename):
    return static_file(filename, root=STATIC_ROOT)

@get(URL_PREFIX + '/')
def page():
    return template('mainPage', poem=poem)

@post(URL_PREFIX + '/')
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

# @get('/poetry')
# def scores_view():
#     c = db_connect()
#     c.execute('SELECT poem FROM Poems order by written_date DESC')
#     data = c.fetchall()
#     c.close()

#     return template('poetry', data=data)

if DEBUG:
    run(host='localhost', port=8080, debug=True)
else:
    run(server='cherrypy')



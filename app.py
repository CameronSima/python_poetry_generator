import random
import os
import sqlite3
import json

from time import strftime
from bottle import route, run, template, get, post, redirect, request, TEMPLATE_PATH, static_file

import markov

TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))

DEBUG = True
poem = None

if DEBUG:
    URL_PREFIX = ''
    STATIC_ROOT = '/home/cameron/Projects/python_poetry_generator/static'
else:
    URL_PREFIX = '/poetry_generator'
    STATIC_ROOT = '/home/cameron/python_poetry_generator/static'

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

if not DEBUG:
    @route('/poetry_generator')
    def redirect_main():
        return template('mainPage')

@get(URL_PREFIX + '/')
def page():
    try:
        return template('mainPage', poem=poem)
    except:
        return template('mainPage', poem="Oops...Something went wrong. Please try again!")

@post(URL_PREFIX + '/')
def enter_score():
    now = strftime("%Y-%m-%d %H:%M:%S")
    global poem
    poem = markov.write(request.forms)

    redirect(URL_PREFIX + '/')

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



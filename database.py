from flask import g
import sqlite3

def connect_db():
    sql = sqlite3.connect('/Users/Utilizador/Google Drive/Flask/TheUltimateFlaskCourse/qanswer/questions.db')
    sql.row_factory = sqlite3.Row   # dicionários em vez de tuplas
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
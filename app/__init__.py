"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch143fb3cv203bunaikg-a.oregon-postgres.render.com",

        database="todo_pxmw",
        user="todo_pxmw_user",
        password="zQsiSa6i7XTX2htft4hI53BnahsOb9rd")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

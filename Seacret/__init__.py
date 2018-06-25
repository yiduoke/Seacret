from flask import Flask, flash, render_template, request, session, redirect, url_for
import sqlite3
import os
import utils.dbHelper as db
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def root():
    db.createTable('seacrets', [['message', 'TEXT']])
    return render_template("home.html")
#later add the rolling dice/probability for receiving or writing

@app.route("/submitted", methods=["POST"])
def get_message():
    seacret = request.form['seacret']
    print seacret
    db.addMessage(seacret)
    return render_template("submitted.html")
    

if __name__ == "__main__":
    app.debug = True
    app.run()
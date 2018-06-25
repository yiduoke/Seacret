from flask import Flask, flash, render_template, request, session, redirect, url_for
import sqlite3
import os
import random
import utils.dbHelper as db
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def root():
    db.createTable('seacrets', [['message', 'TEXT']])

    num_rows = db.numberRows() * 1.0
    first_number = random.uniform(0, num_rows-1)
    second_number = random.uniform(0, num_rows / 3)

    real_first = first_number
    first_number = int(round(first_number))
    retrieved = db.retrieveNth(first_number)[0]
    print retrieved
    print "that was the message!!!!"

    first_number = real_first
    print "first number is " + str(first_number)
    print "second number is " + str(second_number)
    
    # display a message
    if (first_number < second_number):
        return render_template("message.html", message = retrieved)

    # else just the message form
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
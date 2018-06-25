import sqlite3
from datetime import datetime
from calendar import monthrange
import os

timezone = ''
dbPath = os.path.dirname(__file__) or '.'
dbPath += '/../data/db.db'

def openDb():
    db = sqlite3.connect(dbPath, detect_types = sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    return db

def getCursor(db):
    c = db.cursor()
    return c
    
def saveDb(db):
    db.commit()

def closeDb(db):
    db.close()

###############################################
#run once, creates a table
#columns argument should be a list of sublists where first element is column name, 2nd element is sqlite type in string form
#example: createTable('users', [ ['username', 'TEXT PRIMARY KEY'], ['password', 'TEXT'] ])
def createTable(tableName, columns):
    db = openDb()
    cursor = getCursor(db)
    #using IF NOT EXISTS to avoid errors
    cmdString = 'CREATE TABLE IF NOT EXISTS ' + str(tableName) + '('
    
    for column in columns:
        cmdString += str(column[0]) + ' ' + str(column[1]) + ', '
        
    #to get rid of the extra ', ' at the end
    cmdString = cmdString[:-2]
    cmdString += ');'
    
    cursor.execute(cmdString)
    saveDb(db)
    closeDb(db)

#inserts row data into a table
#columns argument is a list of the columns to be entered
#values argument is a list of the corresponding values in the same order
#example: insertRow('users', ['username', 'password'], ['"md"', '"pw"'])
def insertRow(tableName, columns, values):
    db = openDb()
    cursor = getCursor(db)
    
    cmdString = 'INSERT INTO '
    cmdString += str(tableName) + ' ('
    
    for column in columns:
        cmdString += str(column) + ', '
        
    #to get rid of the extra ', ' at the end
    cmdString = cmdString[:-2]
    cmdString += ') VALUES ('
    
    for value in values:
        cmdString += str(value) + ', '
        
    #to get rid of the extra ', ' at the end
    cmdString = cmdString[:-2]
    cmdString += ');'
    
    cursor.execute(cmdString)
    saveDb(db)
    closeDb(db)

def addMessage(message):
    db = openDb()
    cursor = getCursor(db)
    addMessage = "INSERT INTO seacrets (message) VALUES ('%s');" % (message)
    cursor.execute(addMessage)
    
    saveDb(db)
    closeDb(db)
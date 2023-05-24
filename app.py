from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

app = Flask(__name__)
db_connection = db.connect_to_database()

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_leeje7'
app.config['MYSQL_PASSWORD'] = '8989' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_leeje7'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)


# Routes

@app.route('/')
def root():
    return render_template("index.j2")

@app.route('/index.j2')
def index():
    return render_template("index.j2")

@app.route('/companies.j2')
def companies():
    return render_template("companies.j2")

@app.route('/drugs.j2')
def drugs():
    return render_template("drugs.j2")

@app.route('/patients.j2')
def patients():
    return render_template("patients.j2")

@app.route('/prescriptions.j2')
def prescriptions():
    return render_template("prescriptions.j2")

@app.route('/routes.j2')
def routes():
    return render_template("routes.j2")

@app.route('/frequencies.j2')
def frequencies():
    return render_template("frequencies.j2")

@app.route('/companies_drugs.j2')
def companies_drugs():
    return render_template("companies_drugs.j2")

@app.route('/test_companies')
def test_companies():
    query = "SELECT * FROM Companies;"

    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = json.dumps(cursor.fetchall())

    return results
# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 49171)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port) 
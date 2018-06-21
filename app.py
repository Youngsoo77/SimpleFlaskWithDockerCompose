# -*- coding: utf-8 -*-
import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

DB_USER = os.environ['DBUSER']
DB_PASSWORD = os.environ['DBPASS']
DB_ADDR = os.environ['DBADDR']

app = Flask(__name__)
DB_URI = 'mysql+pymysql://'+DB_USER+':'+DB_PASSWORD+'@'+DB_ADDR+':3306/flaskappdb?charset=utf8'
# DB_URI = ''
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'youngsoo'

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html', name=os.environ['YOUNGSOO'])    


@app.route('/result', methods=['POST'])
def result():
    if request.method == "POST":
        fields = [key for key in request.form]                                      
        values = [request.form[key] for key in request.form]
        data = dict(zip(fields, values))
    return jsonify(data) 


if __name__ == '__main__':
    app.run(debug=True)

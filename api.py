import flask
from flask import render_template,request
from flask import jsonify
from finance import *   

app=flask.Flask(__name__)
app.config["DEBUG"]=True

@app.route("/",methods=['GET'])
def getStockInfo():
        return render_template('home.html')

@app.route("/stock",methods=['POST'])
def getStock():
    
   
    data=getInfo(request.form['name'].upper())
    return render_template('stock.html',data=data)
   


app.run()


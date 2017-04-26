#coding:utf-8
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
	return '<center><h1>Olá essa é a página inicial</h1></center>'
 
@app.route("/status")
def status():
	return render_template ('status.py')

@app.route("/menu")
def menu():
	return render_template ('menu.html')

@app.route("/rodape")
def rodape():
	return render_template ('rodape.html')





if __name__ == "__main__":
 	app.run(debug=True)


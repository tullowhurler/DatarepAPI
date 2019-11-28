#!flask/bin/python 
from flask import Flask 

app = Flask(__name__, static_url_path='', static_folder='../')
 #app = Flask(__name__)
 
#@app.route('/') 
#def index():     
#    return"Hello, World!" 

@app.route('cars')
def getAll():
    return "in getAll"

@app.route('cars/<int:reg>')
def getAll(id):
    return "in find By REG for reg"+str(reg)

if __name__ == '__main__' :     
    app.run(debug= True)
#!flask/bin/python 
from flask import Flask 

app = Flask(__name__, static_url_path='', static_folder='../')
 #app = Flask(__name__)
 
#@app.route('/') 
#def index():     
#    return"Hello, World!" 

@app.route('/cars')
def getAll():
    return "in getAll"

@app.route('/cars/<int:reg>')
def findByReg(reg):
    return "in find By REG for reg"+str(reg)

@app.route('/cars', methods=['POST'])
def create():
    return "in create"

@app.route('/cars/<int:reg>', methods=['PUT'] )
def update(reg):
    return "in update for reg"+str(reg)

@app.route('/cars/<int:reg>', methods=['DELETE'])
def delete(reg):
    return "in delete for reg"+str(reg)



if __name__ == '__main__' :     
    app.run(debug= True)
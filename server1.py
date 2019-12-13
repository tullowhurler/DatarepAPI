#!flask/bin/python 
from flask import Flask, jsonify

app = Flask(__name__, static_url_path='', static_folder='../')
 
cars=[ 
    {"reg": 131, "make": "AudiA5", "Price":"15000","Mileage":"25000"},
    {"reg": 132, "make": "AudiA6", "Price":"20000","Mileage":"20000"},
    {"reg": 141, "make": "AudiA7", "Price":"30000","Mileage":"15000"}
]
NextId=4

 #app = Flask(__name__)
 
#@app.route('/') 
#def index():     
#    return"Hello, World!" 

#curl "http://127.0.0.1:5000/cars"
@app.route('/cars')
def getAll():
    return jsonify(cars)

@app.route('/cars/<int:reg>')
def findByReg(reg):
    foundCars = list(filter(lambda c: c['reg'] == reg, cars))
    if len(foundCars) == 0:
        return jsonify ({}) , 204 
    
    return jsonify (foundCars[0]) 

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
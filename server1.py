#!flask/bin/python 
from flask import Flask, jsonify, request, abort
from carDAO import carDAO
import mysql.connector 

app = Flask(__name__, static_url_path='', static_folder='../')

#app = Flask(__name__)
 
#@app.route('/') 
#def index():     
#    return"Hello, World!" 

#curl "http://127.0.0.1:5000/cars"
@app.route('/cars')
def getAll():
    #print("in getall")
    results = carDAO.getAll()
    return jsonify(results)

# curl "http://127.0.0.1:5000/cars/131"
@app.route('/cars/<int:id>')
def findById(id):
    foundCars = carDAO.findByID(id) 

    return jsonify (foundCars) 

# curl -i -H "Content-Type:application/json" -X POST -d "{\"make\":\"AudiA3\",\"Price\":\"10000\",\"Mileage\":\"5000\"}" http://127.0.0.1:5000/cars
@app.route('/cars', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking
    car = {
        "make": request.json['make'],
        "Price": request.json['Price'],
        "Mileage": request.json['Mileage'],
        
    }
    values =(car['make'],car['Price'],car['Mileage'])
    newId = carDAO.create(values)
    car['id'] = newId
    return jsonify(car)

# curl -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"AudiA3\",\"Price\":\"10000\",\"Mileage\":\"5000\"}" http://127.0.0.1:5000/cars/1
@app.route('/cars/<int:id>', methods=['PUT'] )
def update(id):
    foundCarr = carDAO.findByID(id)
    if not foundCarr: 
        abort(404)

    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)
    if 'Mileage' in reqJson and type(reqJson['Mileage']) is not int:
        abort(400)
        
    if 'make' in reqJson:
        foundCar['make'] = reqJson['make']
    if 'Price' in reqJson:
        foundCar['Price'] = reqJson['Price']
    if 'Mileage' in reqJson:
        foundCar['Mileage'] = reqJson['Mileage']
    
    values = (foundCar['make'],foundCar['Price'],foundCar['Mileage'], foundCars['id'])
    # will not update for some reason, everything is working fine
    carDAO.update(values)
    return jsonify(foundCar)

@app.route('/cars/<int:id>', methods=['DELETE'])
def delete(id):
    carDAO.delete(id)
    return jsonify({"done":True})



if __name__ == '__main__' :     
    app.run(debug= True)
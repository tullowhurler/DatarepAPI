#!flask/bin/python 
from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='../')
 
cars=[ 
    {"id": 1, "make": "AudiA5", "Price":"15000","Mileage":"25000"},
    {"id": 2, "make": "AudiA6", "Price":"20000","Mileage":"20000"},
    {"id": 3, "make": "AudiA7", "Price":"30000","Mileage":"15000"}
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

# curl "http://127.0.0.1:5000/cars/131"
@app.route('/cars/<int:id>')
def findById(id):
    foundCars = list(filter(lambda c: c['id'] == id, cars))
    if len(foundCars) == 0:
        return jsonify ({}) , 204 

    return jsonify (foundCars[0]) 

# curl -i -H "Content-Type:application/json" -X POST -d "{\"make\":\"AudiA3\",\"Price\":\"10000\",\"Mileage\":\"5000\"}" http://127.0.0.1:5000/cars
@app.route('/cars', methods=['POST'])
def create():
    global NextId
    if not request.json:
        abort(400)
    # other checking
    car = {
        "id": NextId,
        "make": request.json['make'],
        "Price": request.json['Price'],
        "Mileage": request.json['Mileage'],

    }
    NextId +=1
    cars.append(car)
    return jsonify(car)

# curl -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"AudiA3\",\"Price\":\"10000\",\"Mileage\":\"5000\"}" http://127.0.0.1:5000/cars/1
@app.route('/cars/<int:id>', methods=['PUT'] )
def update(id):
    foundCars = list(filter(lambda c: c['id']== id, cars))
    if (len(foundCars) == 0):
        abort(404)
    foundCar = foundCars[0]
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
    
    return jsonify(foundCar)

    return "in update for id"+str(id)

@app.route('/cars/<int:id>', methods=['DELETE'])
def delete(id):
    return "in delete for id"+str(id)



if __name__ == '__main__' :     
    app.run(debug= True)
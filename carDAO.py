import mysql.connector 
class CarDAO:     
    db=""     
    def __init__(self):          
        self.db = mysql.connector.connect(         
            host="localhost",         
            user="root",         
            password="",         
            #user="datarep",  # this is the user name on my mac         
            # #passwd="password" # for my mac         
            database="datarepresentation"         
            )     
    def create(self, values):         
        cursor = self.db.cursor()         
        sql="insert into car (make, Price, Mileage) values (%s,%s,%s)"         
        cursor.execute(sql, values) 
         
        self.db.commit()         
        return cursor.lastrowid

    def getAll(self):         
        cursor = self.db.cursor()         
        sql="select * from car"         
        cursor.execute(sql)         
        result = cursor.fetchall()         
        return result

    def findByID(self, id):         
        cursor = self.db.cursor()         
        sql="select * from car where id = %s"         
        values = (id,) 

        cursor.execute(sql, values)         
        result = cursor.fetchone()         
        return result   

    def update(self, values):         
        cursor = self.db.cursor()         
        sql="update car set make= %s, Price=%s, Mileage=%s,  where id = %s"         
        cursor.execute(sql, values)         
        self.db.commit()

    def delete(self, id):         
        cursor = self.db.cursor()         
        sql="delete from car where id = %s"         
        values = (id,) 

        cursor.execute(sql, values) 
        
        self.db.commit()         
        print("delete done")

    def convertToDictionary(self,result):
        colnames=['id','make','Price','Mileage']
        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

carDAO = CarDAO()
 
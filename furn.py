from flask import Flask,request
from flask_restful import Resource,Api
import json


app = Flask(__name__)
api = Api(app)


response = []

class home(Resource):
    def get(self):
        return {"message" : "Hey, welcome to dummy furniture api"}

class getAllFurns(Resource):
    def get(self):
        f = open('furniture.json')
        furnData = json.load(f)

        try:
            response = furnData['all']
            return response,200
        except Exception as e:
            return e.message, 500

        #print(furnData)
        
        print(furnData)



# class getAllFurns:
#     def get(self):
#         f = open('furniture.json')
#         furnData = json.load(f)
#         print(furnData)
#         f.close()
        

api.add_resource(home,'/',endpoint = '')
api.add_resource(getAllFurns,'/all',endpoint = 'all' )

if __name__ == '__main__':
    app.run(debug=True)

# print("works")
# x = getAllFurns()
# x.get()
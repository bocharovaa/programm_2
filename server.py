from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

#словарь доступных интернет-услуг
services = {
    1: {"name": "Base", "speed(mb/s)": 500},
    2: {"name": "Advance", "speed(mb/s)": 1000}
}

#парсер запросов
parser = reqparse.RequestParser()
parser.add_argument("name", type=str) #аргумент названия
parser.add_argument("speed(mb/s)", type=int)  #аргумент скорости

class Main(Resource):
    #реализация метода GET
    def get(self, service_id):
        if service_id == 0:
            return services
        else:
            return services[service_id]

    def get_ids(self):
        for n,v in enumerate(services):
            print(n)

    #реализация метода POST
    def post(self, service_id):
        services[service_id] = parser.parse_args()
        return service_id


api.add_resource(Main, "/api/services/<int:service_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")

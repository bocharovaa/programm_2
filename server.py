import flask
from flask_restful import Api, Resource, reqparse
from ssePublisher import Publisher
from time import sleep


app = flask.Flask(__name__)
api = Api()
publisher = Publisher()

#словарь доступных интернет-услуг
services = {
    1: {"name": "Base", "speed(mb/s)": 500},
    2: {"name": "Advance", "speed(mb/s)": 1000}
}

#парсер запросов
parser = reqparse.RequestParser()
parser.add_argument("name", type=str) #аргумент названия
parser.add_argument("speed(mb/s)", type=int)  #аргумент скорости

class Events(Resource):
    def get(self):
        return flask.Response(publisher.subscribe(), content_type='text/event-stream')
    
class Main(Resource):
    #реализация метода GET
    def get(self, service_id):
        if service_id == 0:
            result = services
        else:
            result = services[service_id]
            
        for i in range(1,10):
            publisher.publish("processing ... {} %".format(i*10))
            sleep(0.1)
            
        publisher.publish("Done!")
        publisher.publish(result)
        
        return result


    #реализация метода POST
    def post(self, service_id):
        services[service_id] = parser.parse_args()
        for i in range(1,10):
            publisher.publish("processing ... {} %".format(i*10))
            sleep(0.1)
        publisher.publish("Done!")
        publisher.publish(services[service_id])
        
        return services[service_id]



api.add_resource(Main, "/api/services/<int:service_id>")
api.add_resource(Events, "/api/services/subscribe")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")

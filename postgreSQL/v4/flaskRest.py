from flask import Flask
from flask_restful import Resource, Api

import fromV2

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'title': 'First REST API post',
                'slug': 'rest-api-1',
                'status': 'publish',
                'content': 'this is the content post',
                'author': '1',
                'excerpt': 'Exceptional post!',
                'format': 'standard'}
class test2(Resource):
    def get(self):
        return [["row 1, col 1","row 1, col 2","row 1, col 3","row 1, col 4"],["row 2, col 1","row 2, col 2","row 2, col 3","row 2, col 4"],["row 3, col 1","row 3, col 2","row 3, col 3","row 3, col 4"]]


class test1(Resource):
    def get(self):
        return fromV2.results_list[0][0]


api.add_resource(HelloWorld, '/1')
api.add_resource(test1, '/2')
api.add_resource(test2, '/3')

if __name__ == '__main__':
    app.run(debug=True)

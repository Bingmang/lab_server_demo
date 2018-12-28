from flask_restful import Resource


class Hello(Resource):
    def __init__(self):
        super(Hello, self).__init__()
        self.message = 'Hello Afish'

    def get(self):
        return {'message': self.message}

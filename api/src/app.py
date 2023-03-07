from flask import Flask
from flask_restful import Api

from resources.de_enigma_resource import DeEnigmaResource
from resources.enigma_resource import EnigmaResource

app = Flask(__name__)
api = Api(app)


api.add_resource(EnigmaResource, '/enigma')
api.add_resource(DeEnigmaResource, '/de_enigma')


if __name__ == '__main__':
    app.run(debug=True)
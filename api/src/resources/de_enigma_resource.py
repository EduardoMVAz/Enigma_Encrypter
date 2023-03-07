from flask_restful import Resource
from flask import request

import sys
sys.path.append('../../')

from encrypter.enigma import Enigma


class DeEnigmaResource(Resource):
    
    def get(self):

        try:
            corpo = request.get_json(force=True)
        except:
            return {'error': 'Error parsing the JSON'}, 400
        

        if 'message' not in corpo:
            return {'error': 'Missing message'}, 400
        
        message = corpo['message']

        if 'seed' not in corpo:
            enigma = Enigma()
        else:
            enigma = Enigma(corpo['seed'])


        try:
            decrypted_message = enigma.de_enigma(message)
    
            return {'decrypted message': decrypted_message}, 200
        except:
            return {'error': 'Error encrypting the message'}, 400
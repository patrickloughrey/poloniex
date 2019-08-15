from flask import Flask, request
from flask_restplus import Api, Resource, fields
from poloniex import Poloniex
from flask import abort
import requests
import json


app = Flask(__name__)
api = Api(app, title='Poloniex REST API',
        description='Interact with the Poloneix cryptocurrency exchange')

ns = api.namespace('poloneix', description='Various, unique functions that return specific data according to endpoint')

taxes_model = api.model('API Model', {
    'key': fields.String(description="A User's API Key", required=True),
    'secret': fields.String(description="A User's API Secret", required=True)
})

volume_model = api.model('API Model', {
    'key': fields.String(description="A User's API Key", required=True),
    'secret': fields.String(description="A User's API Secret", required=True),
    'amount': fields.Integer(description="The top 1, 5, 10, 25, or 50 cryptocurrencies currently by volume", required=True)
})

@ns.route('/taxes')
class Taxes(Resource):
    @api.expect(taxes_model)
    def post(self):
        return {'Hello': 'World'}

@ns.route('/volume')
class Volume(Resource):
    @api.expect(volume_model)
    def post(self):
        if request.method == 'POST':
            data = json.loads(request.data)
            key = data['key']
            secret = data['secret']
            amount = data['amount']
        else:
            abort(400, "The HTTP request type must be a POST\n")

        req = requests.get('https://poloniex.com/public?command=returnCurrencies')
    
        for key, value in req.json().items():
            print(key, value)


if __name__ == '__main__':
    app.run(debug=True)

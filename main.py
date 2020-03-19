from flask import Flask
from flask_restful import Api, Resource, reqparse
from keras.models import Sequential
from keras.layers.core import Dense
import numpy as np
from keras.models import load_model

def pred(num1, num2):
    data = np.array([[num1, num2]])
    model2 = load_model("model.h5")
    model.predict(data)


app = Flask(__name__)
api = Api(app)

options = [
    {
        "num1": "0",
        "num2": "0",
        "ans": "0"
    },
    {
        "num1": "0",
        "num2": "1",
        "ans": "1"
    },
    {
        "num1": "1",
        "num2": "0",
        "ans": "1"
    },
    {
        "num1": "1",
        "num2": "1",
        "ans": "0"
    }
]

class User(Resource):
    def get(self, num):
        number1 = num[0]
        number2 = num[1]
        for opt in options:
            if(number1 == opt["num1"] and number2 == opt["num2"]):
                return opt, 200
        return "Option not found", 404
    def post(self, num):
        number1 = num[0]
        number2 = num[1]

        opto = [
            {
                "num1": str(number1),
                "num2": str(number2),
                "ans": pred(number1, number2)
            }
        ]


api.add_resource(User, "/user/<string:num>")

app.run(debug=True)
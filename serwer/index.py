from flask import Flask
from flask_cors import CORS

questions = [{
    "question": "Jak ci mija dzien",
    "answers": ["slabo","normalnie","dobrze"],
    "image": "obrazeksrc",
    "description" : "Jak dzisiaj sie cos stalo to mozesz mi powiedziec"
  },{
    "question": "Co jadleś",
    "answers": ["banana","płatki","ziemniaki"],
    "image": "obrazeksrc",
    "description" : "Co miałes na śnadanie?"
  }]


app = Flask(__name__)
CORS(app)

app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response
    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/question/<int:questionId>',methods=['GET'])
def get_question(questionId):
    return questions[questionId]    
from flask import Flask,send_file,request
from flask_cors import CORS
import pandas
from sklearn import tree

from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv('./CzyZagram.csv',sep=";")



d = {'RPG': 0, 'RoqueLike': 1, 'RTS': 2}
df['Gatunek'] = df['Gatunek'].map(d)

d = {'turowa': 0, 'akcji': 1, 'shooter':2,
     'platform':3,'autoBattler':4, 'baseBuilding':5}
df['Typ'] = df['Typ'].map(d)

d = {'rozwinieta': 0, 'prosta': 1}
df['Historia'] = df['Historia'].map(d)

d = {'dobre': 0, 'slabe': 1}
df['Sterowanie'] = df['Sterowanie'].map(d)

d = {'dluga': 0, 'krotka': 1}
df['Dlugosc'] = df['Dlugosc'].map(d)

d = {'zagram': 1, 'nie zagram': 0}
df['Go'] = df['Go'].map(d)

features = ['Gatunek', 'Typ','Historia' ,'Sterowanie', 'Dlugosc']

X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

inputs = [[0,0,0,0,0]]

# print(dtree.predict([[0, 0, 0, 0, 0]]))



# data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
# graph = pydotplus.graph_from_dot_data(data)
# graph.write_png('mydecisiontree.png')

# img=pltimg.imread('mydecisiontree.png')
# imgplot = plt.imshow(img)
# plt.show()


questions = [{
    'question': 'Wybierz gatunek gry',
    'answers': [{'name':'RPG','id':0,'image':'RPG.jpg', 'description': 'Gry w których gramy jedna lub drużyna postaci, rozwijając naszą postać czy drużyne w walce i poznając świat z ich strony'}, 
                {'name':'RoqueLike','id':1,'image':'RoqueLike.jpg','description':'Gry z randomowymi wygenorowanymi poziomamy przez co każda rozgrywka jest inna'}, 
                {'name':'RTS','id':2, 'image':'RTS.jpg','description':'Gry w których wcialmy się w dowódce miasta czy armii i musimy użyc strategii aby pokonać przeciwnika'} ],
    'image': 'Gatunek.jpg',
    'description' : 'Jaki gatunek gry chcesz zagrac?'
  },
  {
    'question': 'Wybierz typ gry',
    'image': 'Types.jpg',
    'description' : 'Wybierz typ gatunku jakiego wybrałes wcześniej'
  },
  {
    'question': 'historia gry',
    'answers':[{'name':'rozwinieta','id': 0,'image':'Advanced.jpg','description':'Historia gry ma wiele wątków pobocznych i jest wciągająca'},
               {'name':'prosta','id': 1,'image':'Simple.jpg','description':'Historia gry ma tylko wątek głowny albo nie ma jej wcale'}],
    'image': 'History.jpg',
    'description' : 'Jak bardzo bedzie rozwinięta historia gry?'
  },
  {
    'question': 'Sterowanie gry',
    'answers':[{'name':'dobre','id': 0,'image':'Good.jpg','description':'Sterowanie jest wygodne i jest bardzo elastyczne'},
               {'name':'slabe','id': 1,'image':'Bad.jpg','description':'Sterowanie przyszkadza w rozgrywce i nie da się go zmienić'}],
    'image': 'Controls.jpg',
    'description' : 'Czy w grze sie fajnie porusza?'
  },
  {
    'question': 'Dlugosc gry',
    'answers':[{'name':'dluga','id': 0,'image':'Long.jpg','description':'Gra jest nie skończona albo Przejście całej gry trwa więcej niż 20h'},
               {'name':'krotka','id': 1,'image':'Short.jpg','description':'Przejście całej gry trwa mnie niż 20h'}],
    'image': 'HowLong.jpg',
    'description' : 'jak długo da się grać w daną gre'
  },  
  {
    'question': 'Finalny wynik',
    'image': 'History.jpg',
    'description' : 'Zagram w dana gre'
  }]


app = Flask(__name__)
CORS(app)

    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/image/<name>", methods=['GET'])
def get_image(name):
    return send_file('./images'+name,mimetype='image/jpg')

@app.route('/question/<int:questionId>',methods=['GET','POST'])
def get_question(questionId):
     if request.method == 'GET':
        return questions[questionId]
     if request.method == 'POST':
        
        body=request.json

        inputs[0][questionId-1]=body['answer']
        #special case
        if (questionId == 1):
            answers=[{'name':'turowa','id':0,'image':'TurnBased.jpg','description':'Gra rpg w których walki rozgrywają się turowo na zmiane'},
                {'name':'akcji','id':1,'image':'Action.jpg','description':'Gra rpg w których walki so szybkie i rozgrywają się w czasie rzeczywistym'},
                {'name':'shooter','id':2,'image':'Shooter.jpg','description':'Gry Roquelike w których głownie strzela się z daleka do przeciwników przez to wymagają one od gracza prezycji'},
                {'name':'platform','id':3,'image':'Platformer.jpg','description':'Gry Roquelike w których skacze się miedzy różnymi przeszkodami aby dość do jakiegos celu'},
                {'name':'autoBattler','id':4,'image':'AutoBattler.jpg','description':'Gry RTS w której walka rozgrywa się sama my tylko wymyślamy strategie naszej armii'},
                {'name':'baseBuilding','id':5,'image':'BaseBuilding.jpg','description':'Gry RTS w której musimy zbudować dobrą baze z której pożniej bedziemy wysyłać jednostki do przeciwnika'}]        


            if(body['answer'] == 0):
              questions[questionId]['answers']=[answers[0],answers[1]]
            if(body['answer'] == 1):
              questions[questionId]['answers']=[answers[2],answers[3]]
            if(body['answer'] == 2):
              questions[questionId]['answers']=[answers[4],answers[5]]

        #getting result
        if (questionId == 5):
            final = dtree.predict(inputs)

            if (final[0] == 1):
              questions[questionId]['description']="Zagram"
              questions[questionId]['image']="Zagram.jpg"
            else:
              questions[questionId]['description']="NieZagram"
              questions[questionId]['image']="NieZagram.jpg"
            inputs[0]=[0,0,0,0,0]
     
 
        return questions[questionId] 








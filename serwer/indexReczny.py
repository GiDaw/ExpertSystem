import rule_engine
from flask import Flask,send_file,request
from flask_cors import CORS
# Define the rules
rules = [

    #RPG turn based
    {
        'condition': "Gatunek == 'RPG' and Typ == 'turowa' and Historia == 'rozwinieta' and Sterowanie == 'dobre' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'turowa' and Historia == 'rozwinieta' and Sterowanie == 'dobre' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'turowa' and Historia == 'rozwinieta' and Sterowanie == 'slabe' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'turowa' and Historia == 'rozwinieta' and Sterowanie == 'slabe' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'turowa' and Historia == 'prosta' and Sterowanie == 'dobre' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'turowa' and Historia == 'prosta' and Sterowanie == 'dobre' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'turowa' and Historia == 'prosta' and Sterowanie == 'slabe' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'turowa' and Historia == 'prosta' and Sterowanie == 'slabe' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },

    #RPG action

    {
        'condition': "Gatunek == 'RPG' and Typ == 'akcji' and Historia == 'rozwinieta' and Sterowanie == 'dobre' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'akcji' and Historia == 'rozwinieta' and Sterowanie == 'dobre' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'akcji' and Historia == 'rozwinieta' and Sterowanie == 'slabe' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'akcji' and Historia == 'rozwinieta' and Sterowanie == 'slabe' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'akcji' and Historia == 'prosta' and Sterowanie == 'dobre' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'akcji' and Historia == 'prosta' and Sterowanie == 'dobre' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'akcji' and Historia == 'prosta' and Sterowanie == 'slabe' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RPG' and Typ == 'akcji' and Historia == 'prosta' and Sterowanie == 'slabe' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },

    #RoqueLike shooter
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'shooter' and Historia == 'rozwinieta' and Sterowanie == 'dobre' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'shooter' and Historia == 'rozwinieta' and Sterowanie == 'dobre' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'shooter' and Historia == 'rozwinieta' and Sterowanie == 'slabe' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'shooter' and Historia == 'rozwinieta' and Sterowanie == 'slabe' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'shooter' and Historia == 'prosta' and Sterowanie == 'dobre' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'shooter' and Historia == 'prosta' and Sterowanie == 'dobre' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'shooter' and Historia == 'prosta' and Sterowanie == 'slabe' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'shooter' and Historia == 'prosta' and Sterowanie == 'slabe' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },

    #RoqueLike platform

    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'platform' and Historia == 'rozwinieta' and Sterowanie == 'dobre' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'platform' and Historia == 'rozwinieta' and Sterowanie == 'dobre' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'platform' and Historia == 'rozwinieta' and Sterowanie == 'slabe' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'platform' and Historia == 'rozwinieta' and Sterowanie == 'slabe' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'platform' and Historia == 'prosta' and Sterowanie == 'dobre' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'platform' and Historia == 'prosta' and Sterowanie == 'dobre' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'platform' and Historia == 'prosta' and Sterowanie == 'slabe' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RoqueLike' and Typ == 'platform' and Historia == 'prosta' and Sterowanie == 'slabe' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },

    #RTS autoBattler

    {
        'condition': "Gatunek == 'RTS' and Typ == 'autoBattler' and Historia == 'rozwinieta' and Sterowanie == 'dobre' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'autoBattler' and Historia == 'rozwinieta' and Sterowanie == 'dobre' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'autoBattler' and Historia == 'rozwinieta' and Sterowanie == 'slabe' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'autoBattler' and Historia == 'rozwinieta' and Sterowanie == 'slabe' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'autoBattler' and Historia == 'prosta' and Sterowanie == 'dobre' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'autoBattler' and Historia == 'prosta' and Sterowanie == 'dobre' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'autoBattler' and Historia == 'prosta' and Sterowanie == 'slabe' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'autoBattler' and Historia == 'prosta' and Sterowanie == 'slabe' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },

    #RTS baseBuilding

    {
        'condition': "Gatunek == 'RTS' and Typ == 'baseBuilding' and Historia == 'rozwinieta' and Sterowanie == 'dobre' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'baseBuilding' and Historia == 'rozwinieta' and Sterowanie == 'dobre' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'baseBuilding' and Historia == 'rozwinieta' and Sterowanie == 'slabe' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'baseBuilding' and Historia == 'rozwinieta' and Sterowanie == 'slabe' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'baseBuilding' and Historia == 'prosta' and Sterowanie == 'dobre' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'baseBuilding' and Historia == 'prosta' and Sterowanie == 'dobre' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'baseBuilding' and Historia == 'prosta' and Sterowanie == 'slabe' and Dlugosc == 'dluga'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'zagram', 'opis': 'zagram'}
    },
    {
        'condition': "Gatunek == 'RTS' and Typ == 'baseBuilding' and Historia == 'prosta' and Sterowanie == 'slabe' and Dlugosc == 'krotka'",
        'action': lambda fact: {'ktora': fact['ktora'], 'wynik': 'nie zagram', 'opis': 'nie zagram'}
    },
    
]

# Function to evaluate rules based on input facts
def evaluate_rules(facts):
    results = []
    for fact in facts:
        for rule in rules:
            try:
                engine = rule_engine.Rule(rule['condition'])
                if engine.matches(fact):
                    results.append(rule['action'](fact))
            except Exception as e:
                print(f"Error processing rule {rule['condition']}: {e}")
    return results


inputs=[0,0,0,0,0]

# Evaluate the rules with the given facts
#results = evaluate_rules(facts)

# Print results
#for result in results:
#    print(f"Auto: {result['ktora']}. Wynik: {result['wynik']}. Opis auta: {result['opis']}.")

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
        global inputs
        body=request.json
        print(questionId)

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

        if(questionId == 2):
            if(body['answer'] == 2 or body['answer']== 4):
               print(questions[questionId-1]['answers'][0]['name'])
               inputs[questionId-1]=questions[questionId-1]['answers'][0]['name']
            elif(body['answer'] == 3 or body['answer']== 5):
               print(questions[questionId-1]['answers'][1]['name'])
               inputs[questionId-1]=questions[questionId-1]['answers'][1]['name']
            else:
               print(questions[questionId-1]['answers'][body['answer']]['name'])
               inputs[questionId-1]=questions[questionId-1]['answers'][body['answer']]['name']
        else:
            print(body['answer'])
            inputs[questionId-1]=questions[questionId-1]['answers'][body['answer']]['name']

        if (questionId == 5):
            fact = [{'ktora': '0', 'Gatunek':inputs[0], 'Typ':inputs[1], 'Historia':inputs[2], 'Sterowanie':inputs[3], 'Dlugosc':inputs[4]}]
            print(fact)
            final = evaluate_rules(fact)
            print(final)
            if (final[0]['wynik'] == 'zagram'):
              questions[questionId]['description']="Zagram"
              questions[questionId]['image']="Zagram.jpg"
            else:
              questions[questionId]['description']="NieZagram"
              questions[questionId]['image']="NieZagram.jpg"
            inputs=[0,0,0,0,0]

        
        return questions[questionId]
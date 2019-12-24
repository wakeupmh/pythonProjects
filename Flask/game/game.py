from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


game1 = Game('Super Mario', 'adventure', 'SNES')
game2 = Game('Pokemon Gold', 'RPG', 'GBA')
list = [game1, game2]


@app.route('/')
def hello():
    return render_template('list.html', props={'title': 'Games', 'games': list})


@app.route('/new')
def new():
    return render_template('new.html')


@app.route('/create', methods=['POST', ])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)
    list.append(game)
    return redirect('/')


app.run(debug=True)

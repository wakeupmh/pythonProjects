from flask import Flask, render_template

app = Flask(__name__)

class Game:
  def __init__(self, name, category, console):
    self.name = name
    self.category = category
    self.console = console

@app.route('/init')
def hello():
  game1 = Game('Super Mario', 'adventure', 'SNES')
  game2 = Game('Pokemon Gold', 'RPG', 'GBA')
  list = [game1, game2]
  return render_template('list.html', props={'title': 'Games', 'games': list})

app.run()
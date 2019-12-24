from flask import Flask, render_template

app = Flask(__name__)

@app.route('/init')
def hello():
  list= ['Tetris', 'Super Mario', 'Pokemon Gold']
  return render_template('list.html', props={'title': 'Games', 'games': list})

app.run()
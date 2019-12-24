from flask import Flask, render_template

app = Flask(__name__)

@app.route('/init')
def hello():
  return render_template('list.html', title='Games')

app.run()
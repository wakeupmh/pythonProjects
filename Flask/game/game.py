from flask import Flask

app = Flask(__name__)

@app.route('/init')
def hello():
  return '<h1> Hello Flask </h1>'

app.run()
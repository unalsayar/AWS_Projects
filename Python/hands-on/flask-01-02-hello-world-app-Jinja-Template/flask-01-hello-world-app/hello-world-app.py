from flask import Flask

app = Flask(__name__)

@app.route('/')
def first():
    return "Hello World from Flask!!!"

@app.route('/second')
def second():
    return "Alles Gut!!!"

@app.route('/third/subthird')
def third():
    return "Auf Wiedersehen!!!"

@app.route('/fourth/<string:id>')
def fourth(id):
    return f'Id number of this page is {id}'


if __name__ == '__main__':
    app.run(debug=True)


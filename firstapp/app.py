from flask import Flask

app = Flask(__name__) # create application

@app.route('/') # index route; default end point
def index():
    return "<h1>hello world</h1>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True) # debug for dev, not prod

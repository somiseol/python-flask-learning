from flask import Flask, request, make_response

app = Flask(__name__) # create application

@app.route('/') # index route; default end point
def index():
    return "<h1>hello world</h1>"

@app.route('/hello')
def hello():
    return "hello"


# url processor

@app.route('/greet/<name>')
def greet(name):
    return f'hello {name}'

@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    return f'{num1} + {num2} = {num1 + num2}' # values named in route() are strings, so will be concatenated

@app.route('/sum/<int:num1>/<int:num2>') # need to typecast
def sum(num1, num2):
    return f'{num1} + {num2} = {num1 + num2}'


# request instance

# 127.0.0.1:5555/handle_url_params?name=mike&greeting=hello
@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys(): # make sure that you have all parameters
        greeting = request.args.get('greeting')
        name = request.args['name']
        return f'{greeting}, {name}'
    else:
        return 'some parameters are missing'


# methods

@app.route('/lorem', methods=['GET','POST']) # GET is for getting info, POST is for submitting info, PUT for updating info, DELETE is for deleting info
def lorem():
    if request.method == 'GET':
        return 'GET request made\n'
    elif request.method == 'POST':
        return 'POST request made\n'
    else:
        return 'you will never see this message\n'


# status codes

@app.route('/ipsum')
def ipsum():
    return 'ipsum', 200 # 200 is OK


# custom response
@app.route('/dolor')
def dolor():
    response = make_response('dolor\n')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True) # debug for dev, not prod

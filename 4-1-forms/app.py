from flask import Flask, render_template, request, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST']) # GET iot get the html page, POST iot submit the form
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # get the values of the below keys from the template
        username = request.form['username']
        password = request.form.get('password')

        if username == 'abc' and password == '123':
            return 'Success'
        else:
            return 'failure'

if __name__ == '__main__':
    app.run(debug=True)

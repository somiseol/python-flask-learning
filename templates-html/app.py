from flask import Flask, render_template
# render_template(template_name_or_list) is for returning html file instead of plain text in functions like index()

app = Flask(__name__, template_folder='templates')
# templates directory

@app.route('/')
def index():
    myvalue = 'lorem'
    myresult = 10 + 20
    mylist = [1, 2, 3, 4, 5]
    return render_template('index.html', myvalue=myvalue, myresult=myresult, random_value='ipsum', mylist=mylist) # values will be passed on to the html template


@app.route('/other')
def other():
    return render_template('other.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

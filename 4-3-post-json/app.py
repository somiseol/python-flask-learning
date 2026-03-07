import os, pandas, uuid
from flask import Flask, render_template, request, url_for, Response, send_from_directory

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


@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain': # display text file content
        return file.read().decode()
    elif file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or file.content_type == 'application/vnd.ms-excel': # display excel file content (requires pandas and openpyxl)
        data_frame = pandas.read_excel(file)
        return data_frame.to_html()


@app.route('/excel_to_csv', methods=['POST'])
def excel_to_csv():
    file = request.files['file'] 
    data_frame = pandas.read_excel(file)

    response = Response(
        data_frame.to_csv(),
        mimetype='text/csv', # content type
        headers={ 
            'Content-Disposition': 'attachment; filename=result.csv' # specify download name 
        }
    )

    return response



@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']
    
    df = pandas.read_excel(file)
    
    if not os.path.exists('Downloads'): # if the directory "Downloads" doesn't exist, then make it
        os.makedirs('Downloads')

    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('Downloads', filename))

    return render_template('download.html', filename=filename)



@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename, download_name='result.csv')



if __name__ == '__main__':
    app.run(debug=True)


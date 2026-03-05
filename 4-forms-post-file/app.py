from flask import Flask, render_template, request, send_from_directory
import os
import uuid

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST']) # allow GET and POST requests (default is GET only)
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form['username'] # get value from key
        password = request.form.get('password')

        if username == 'song' and password == '1234':
            return 'Success'
        else:
            return 'Fail'
    return render_template('index.html')

@app.route('/file_upload', methods=['POST'])
def file_upload():
    # output the content of the txt file

    file = request.files['file']
    # if file.content_type == 'text/plain':
    #   return file.read().decode()
    # elif file.content_type == 'different_content_type':
    #   return file.decode_file()
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename = f'{uuid.uuid4()}.txt'
    return render_template('download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename, download_name='result.txt')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

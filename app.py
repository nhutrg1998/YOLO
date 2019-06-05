import os
import subprocess
import shlex
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def solve(): 
    target = os.path.dirname(os.path.abspath(__file__))
    static = '/'.join([target, 'static'])

    file = request.files['file']
    filename = file.filename.split('.')[0]
    input_file = '/'.join([target, file.filename])
    file.save(input_file)

    for file in os.listdir(static):
        os.unlink('/'.join([static, file]))

    output_file = '/'.join([static, '.'.join([filename, 'jpg'])])
    subprocess.call(shlex.split('./shell.sh {} {}'.format(input_file, output_file)))

    while len(os.listdir(static)) == 0:
        pass

    return render_template('result.html', detected_image = '/'.join(['../static', '.'.join([filename, 'jpg'])]))

if __name__ == "__main__":  
    app.run(debug=True)


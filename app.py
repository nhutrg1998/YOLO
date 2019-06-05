import os
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def solve(): 
    target = os.path.dirname(os.path.abspath(__file__))
    res = '/'.join([target, 'static', 'output.jpg'])
    print(res)
    if os.path.exists(res):
        os.remove(res)

    file = request.files['file']
    extension = file.filename.split('.')[1]
    destination = '/'.join([target, '.'.join(['input', extension])])
    file.save(destination)

    subprocess.call(['./shell.sh'])

    while not os.path.isfile(res):
        pass

    return render_template('result.html', detected_image = "../static/output.jpg")

if __name__ == "__main__":  
    app.run(debug=True)


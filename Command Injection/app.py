from flask import *
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    get = request.args.get('Ping')
    try:
        if get:
            command = 'ping -c 4 ' + get
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            rt = render_template('index.html', pinganswer=result)
        else:
            rt = render_template('index.html')
    except:
        render_template('index.html')

    return rt

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000')
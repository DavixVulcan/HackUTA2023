from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}
sock = Sock(app)

@app.route('/')
def index():
    return render_template('index.html')

arry = []

@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        print(data)
        if(data.startswith("newImage")):
            print("recieved url")
            arry.append(data)
            if(len(arry) > 3):
                arry.pop(0)
        else:
            for y in arry:
                ws.send(y)

        # ws.send(data)

app.run()

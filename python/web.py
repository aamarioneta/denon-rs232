from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


def serial_print(msg):
    print("btn_action: " + msg)
    with open("/dev/ttyS0", 'w', encoding='utf-8') as f:
        f.write(msg + "\r")
        print("serial: \n" + msg)


@app.route("/", methods=['GET', 'POST'])
def vis():
    print("request.method: " + request.method)
    if request.method == 'POST':
        btn_action = request.form["btnAction"]
        if btn_action:
            serial_print(btn_action)
        return render_template('index.html', btn_action=btn_action)
    else:
        btn_action = request.args.get('btnAction')
        if btn_action:
            serial_print(btn_action)
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25000)


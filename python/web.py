from flask import Flask
from flask import render_template
from flask import request
import io, os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def vis():
    print("request.method: " + request.method)
    if request.method == 'POST':
        print("request.form btn_action: " + request.form["btnAction"])
        btn_action = request.form["btnAction"]
        print("btn_action: " + btn_action)
        with open("/dev/ttyS0", 'w', encoding='utf-8') as f:
            f.write(btn_action + "\r")
            print("serial: \n" + btn_action)
        return render_template('index.html', btn_action=btn_action)
    else:
        btn_action = request.args.get('btnAction')
        if btn_action:
            print("btn_action: " + btn_action)
            with open("/dev/ttyS0", 'w', encoding='utf-8') as f:
                f.write(btn_action + "\r")
                print("serial: \n" + btn_action)
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25000)

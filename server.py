import flask
import json
import datetime
app = flask.Flask(__name__)


@app.route('/get')
def get():
    with open('data.json', 'r', encoding='utf-8') as file:
        data = file.read()
    return flask.jsonify(json.loads(data))


@app.route('/chat', methods=['POST'])
def chat():
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    name = flask.request.form.get('name')
    msg = flask.request.form.get('msg')
    data.append({'time': time, 'name': name, 'msg': msg})
    with open('data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False))
    return flask.jsonify({'code': 0})


app.run('0.0.0.0', 8000)

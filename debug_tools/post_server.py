from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def post_data():
    data = request.get_json()
    for key, value in data.items():
        print(f'Key: {key}, Value: {value}')
    return 'Received!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

from flask import Flask, jsonify
# import requests
# import json

mensaje =""
destinatariowati =""
datos={}
app = Flask(__name__)

tasks = [
    {
        'prueba': 1,
        'prueba2': u'Buy groceries',
    }
]

@app.route('/index', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=False)
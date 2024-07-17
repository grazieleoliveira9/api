from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message= "Olá, mundo!")


@app.route('/exemple', methods=['GET', 'POST'])
def exemple():
    if request.method == 'GET':
        return jsonify(message='Voce fez uma requisicao GET')
    elif request.method == 'POST':
        return jsonify(message='Voce fez uma requisicao POST')
    
    
@app.route('/hello/<graziele>', methods=['GET'])
def hello_name(graziele):
    return jsonify(message= f"Ola, {graziele}!")

@app.route('/cumprimento/<language>/<name>', methods=['GET'])
def greet_name(language, name):
    greetings = {
        'pt': 'Ola',
        'eng': 'Hello',
        'esp': 'Hola',
        'fr': 'Bonjour'
    }
    
    greeting = greetings.get(language, 'Ola')
    return jsonify(message=f'{greeting}, {name}!')

@app.route('/soma', methods=['GET'])
def sum_values():
    value1 = int(request.args.get('value1', 0))
    value2 = int(request.args.get('value2', 0))
    value3 = int(request.args.get('value3', 0))
    total = value1 + value2 + value3

    return jsonify(message=f'A soma dos valores e {total}')




if __name__ == '__main__':
    app.run(debug=True)
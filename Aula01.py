import os 
from flask import Flask, jsonify, request, render_template
from math import sqrt

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/calculaform', methods=['POST', 'GET'])
def calculaform():
    n1 = request.form['n1']
    n2 = request.form['n2']
    operacao = request.form['operacao']

    print(operacao)

    try:
        n1 = int(n1)
    except ValueError:
        os.abort(404)

    try: 
        n2 = int(n2)
    except ValueError:
        os.abort(404)

    calcula = calculaform()

    if(operacao == 'soma'):
        resultadoCalculado = calcula.somar(n1, n2)
    elif(operacao == 'subtracao'):
        resultadoCalculado = calcula.subtrair(n1, n2)
    else:
        os.abort(404)

    return str(resultadoCalculado)    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5004))
    app.run(host='0.0.0.0', port=port)
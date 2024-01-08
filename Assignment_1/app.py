import numpy as np
from flask import Flask, jsonify

app = Flask(__name__)

def integrate(lower, upper, N):
    dx = (upper - lower) / N
    x = np.linspace(lower, upper, N+1)
    y = np.abs(np.sin(x))
    integral = dx * np.sum(y)
    return integral

@app.route('/integrate/<lower>/<upper>')
def integration_service(lower, upper):
    n_values = [10, 100, 1000, 10000, 100000, 1000000]
    integrals = []
    for n in n_values:
        result = integrate(float(lower), float(upper), n)
        integrals.append(result)

    return jsonify(integrals)

if __name__ == '__main__':
   app.run()

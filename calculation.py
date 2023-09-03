from flask import Flask, jsonify

app = Flask(__name__)

def generate_primes(limit):

    primes = []
    num = 2
    while len(primes) < limit:
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
        num += 1
    return primes

def generate_fibonacci(limit):
   
    fibo = [0, 1]
    while len(fibo) < limit:
        fibo.append(fibo[-1] + fibo[-2])
    return fibo

def generate_odd(limit):
    odds = [i for i in range(1, limit * 2, 2)]
    return odds

@app.route('/primes', methods=['GET'])
def get_primes():
    limit = 15  
    primes = generate_primes(limit)
    return jsonify({"numbers": primes})

@app.route('/fibo', methods=['GET'])
def get_fibo():
    limit = 15  
    fibo = generate_fibonacci(limit)
    return jsonify({"numbers": fibo})

@app.route('/odd', methods=['GET'])
def get_odd():
    limit = 15  
    odds = generate_odd(limit)
    return jsonify({"numbers": odds})
    
    

if __name__ == '__main__':
    app.run(host='localhost', port=8008)

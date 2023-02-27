# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Calculator App!"

@app.route('/add')
def do_add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    res = add(a, b)
    return str(res)

@app.route('/sub')
def do_sub():
    a = int(request.args['a'])
    b = int(request.args['b'])
    res = sub(a, b)
    return str(res)

@app.route('/mult')
def do_mult():
    a = int(request.args['a'])
    b = int(request.args['b'])
    res = mult(a, b)
    return str(res)

@app.route('/div')
def do_div():
    a = int(request.args['a'])
    b = int(request.args['b'])
    res = div(a, b)
    return str(res)

# Single Route Method

ops = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<op>')
def do_math(op):
    a = int(request.args['a'])
    b = int(request.args['b'])
    res = ops[op](a, b)
    return str(res)
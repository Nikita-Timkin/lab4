from flask import Flask, render_template, request
import cmath

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scheme')
def scheme():
    return render_template('scheme.html')


@app.route('/links')
def links():
    return render_template('links.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/quadratic', methods=['POST'])
def quadratic():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])

    discriminant = (b ** 2) - (4 * a * c)
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return render_template('result.html', root1=root1, root2=root2)


if __name__ == '__main__':
    app.run()

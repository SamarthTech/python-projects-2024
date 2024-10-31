from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100
    bmi = weight / (height ** 2)
    return render_template('index.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'f7403cfcdb83eedf55b4e71a55cb4edb'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/forecast', methods=['POST'])
def forecast():
    city = request.form['city']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

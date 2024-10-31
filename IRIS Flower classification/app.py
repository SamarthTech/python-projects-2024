from flask import Flask,url_for,render_template,request
from forms import Inputform
import pickle,numpy as np
import sys
from joblib import dump, load


app = Flask(__name__)


#sys.path.append(r'D:\Flask\webapp')

#print(sys.path)
app.config['SECRET_KEY'] = 'a5a4b1122a72277bfb82e7a5904694a2'

@app.route("/", methods=['GET','POST'])
def predict():
    # initialize the form as the Inputform class object
    form = Inputform()
    if form.is_submitted():
        result = request.form

        # get input values for each of the input fields
        lis = []
        for key,value in result.items():
            if key in ['sl','sw','pl','pw']:
                lis.append(value)
                
        # convert input into np array to use for prediction 
        inputs = np.array([lis])

        # load the model and predict the class
        model = pickle.load(open('model.pkl','rb'))
        pred = model.predict(inputs)

        if pred == 0:
            result = 'Setosa'
        elif pred == 1:
            result = 'Virginica'
        elif pred == 2:
            result = 'Versicolor'

        return render_template('prediction.html', result=result)
    return render_template('predict.html', form = form)

if __name__ == '__main__':
	app.run(debug=True)
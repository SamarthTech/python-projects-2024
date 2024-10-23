# import all packages------------------------------------------
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message

# Create an app------------------------------------------------
app = Flask(__name__)

# database configuration---------------------------------------
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/signdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# email message configuration---------------------------------
# email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "senderemail@gmail.com"
app.config['MAIL_PASSWORD'] = 'created password'  # Replace 'your_gmail_password' with your actual Gmail password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


# Define your model class for the 'signup' table
class Signup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)


# Route for signup page
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_signup = Signup(username=username, email=email)
        db.session.add(new_signup)
        db.session.commit()
        return render_template('index.html', signup_message='User signed up successfully!')



# predictive function
class_labels = ['beagle', 'bulldog', 'dalmatian', 'german-shepherd', 'husky', 'labrador-retriever', 'poodle',
                'rottweiler']
# Function to preprocess and predict
def predict_and_display(img):
    # Load the model
    model = tf.keras.models.load_model('models/fine_tuned_inception.h5')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    confidence_level = np.max(predictions)
    predicted_class_name = class_labels[predicted_class]

    return predicted_class_name, confidence_level



# Route to the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', message='No selected file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join('static', filename)
            file.save(filepath)
            img = image.load_img(filepath, target_size=(224, 224))


            predicted_class, confidence = predict_and_display(img)

            # Send mail alert
            msg = Message('DogBreed Alert', sender='senderemail@gmail.com', recipients=['receiver@gmail.com'])
            # Constructing the email body
            msg.body = f"Dear DogBreed Keeper,\n\nI hope this email finds you well.\n\nI am writing to inform you about an important event regarding your honey bee operations. Our AI model has detected an anomaly in the uploaded image, which we believe requires your attention.\n\nAnalysis Results:\n- Detected Issue: {predicted_class}\n- Confidence Level: {confidence:.2f}%\n\nAttached to this email, you will find a detailed report providing insights into the detected issue, along with recommendations for appropriate actions.\n\nShould you require any further assistance or have any questions, please feel free to contact us.\n\nBest regards,\nYour AI Bot"
            # Send the email
            mail.send(msg)

            alert_message = "Alert Message has been sent to the Dog Breed keeper "
            return render_template('index.html',alert_message=alert_message, image_path=filepath, actual_label=predicted_class,
                                   predicted_label=predicted_class, confidence=confidence)
    return render_template('index.html', message='Upload an image')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}


if __name__ == '__main__':
    app.run(debug=True)
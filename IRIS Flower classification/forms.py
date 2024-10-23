from flask_wtf import FlaskForm
from wtforms import  StringField,PasswordField,SubmitField,BooleanField,FloatField
from wtforms.validators import DataRequired


# create fields for each variable 
class Inputform(FlaskForm):
    sl = FloatField('SEPAL LENGTH (~ 4.3 - 7.9)',validators=[DataRequired()])
    sw = FloatField('SEPAL WIDTH (~ 2.0 - 4.4)',validators=[DataRequired()])
    pl = FloatField('PETAL LENGTH (~ 1.0 - 6.9)',validators=[DataRequired()])
    pw = FloatField('PETAL WIDTH (~ 0.1 - 2.5)',validators=[DataRequired()])
    submit = SubmitField('PREDICT')
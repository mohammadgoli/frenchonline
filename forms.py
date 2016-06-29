from flask_wtf import Form, RecaptchaField
from wtforms import IntegerField, StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class QuestionForm(Form):
	name = StringField("name", validators=[DataRequired(), Length(max=15)])
	email = StringField("email", validators=[Email(), DataRequired()])
	question = TextAreaField("question", validators=[DataRequired(), Length(max=180)])
	recaptcha = RecaptchaField()

class RegisterForm(Form):
	name = StringField("name", validators=[DataRequired(), Length(max=15)])
	email = StringField("email", validators=[Email(), DataRequired()])
	phone = StringField("phone", validators=[DataRequired(), Length(min=10, max=14)])
	class_name = SelectField("class_name", choices=[('1', '1'), ('2', '2'), ('3', '3')])

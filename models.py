from views import db
import datetime 


class Question(db.Model):
	__tablename__ = "questions"

	qid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	question = db.Column(db.String, nullable=False)
	date = db.Column(db.Date, default=datetime.datetime.now())

	def __init__(self, name, email, question):
		self.name = name
		self.email = email
		self.question = question 

	def __repr__(self):
		return self.email

class Register(db.Model):
	__tablename__ = "register"

	reg_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	# family = db.Column(db.String, nullable=False)
	# telegram = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=True)
	phone = db.Column(db.String, nullable=False)
	class_name = db.Column(db.Integer, nullable=False)
	date = db.Column(db.Date, default=datetime.datetime.now())
	payment_verify = db.Column(db.Boolean, default=False)
	

	def __init__(self, name, email, phone, class_name):
		self.name = name
		# self.family = family
		# self.telegram = telegram
		self.email = email
		self.phone = phone
		self.class_name = class_name
		# self.payment_verify = payment_verify

	def __repr__(self):
		return self.phone


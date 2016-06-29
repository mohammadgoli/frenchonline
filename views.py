# _*_ coding: utf-8 _*_
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_mail import Mail, Message 

app = Flask(__name__)
app.config.from_pyfile("_config.py")
db = SQLAlchemy(app)
mail = Mail(app)

from models import Question, Register
from forms import RegisterForm, QuestionForm

from suds.client import Client


description = u'ثبت نام کلاس فرنچ آنلاین'
email = 'user@userurl.ir'  # Optional
mobile = '09123456789'  # Optional

#for telegram usage
from pytg import Telegram

#work with telegram 
tg = Telegram(
    telegram="/home/mohammad/tg/bin/telegram-cli",
    pubkey_file="/home/mohammad/tg/server.pub")
sender = tg.sender


@app.route('/main', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def main():
	error = None 
	form = QuestionForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			newName = form.name.data
			newEmail = form.email.data
			newQuestion = form.question.data
			new_question = Question(
				newName,
				newEmail,
				newQuestion
			)

			msg = Message("Your question submitted",
					recipients = [newEmail],
					sender = 'gli.mhmd@gmail.com',
					body = u'Hello {}\n Your question was submitted through the site frenchonline. We will answer it ASAP ! '.format(newName)
					)

			admin_msg = Message ("You have a new question",
					recipients = ['gli.mhmd@gmail.com'],
					sender = 'gli.mhmd@gmial.com',
					body = u'Your contact {} asked a question with the content \n----------\n"{}"\n----------\n, \nPlease answer through this email {}'.format(newName, newQuestion, newEmail)
				)
			db.session.add(new_question)
			db.session.commit()
			mail.send(msg)
			mail.send(admin_msg)
	return render_template('index.html', form = form, error = error)


@app.route('/register', methods=['GET', 'POST'])
def register():
	error = None 
	form = RegisterForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			newName = form.name.data
			# newFamily = form.family.data
			newEmail = form.email.data
			newPhone = form.phone.data
			newClass = form.class_name.data
			new_student = Register(
				newName,
				newEmail,
				newPhone,
				newClass,	
			)
			db.session.add(new_student)
			db.session.commit()

			sender.send_msg('Mammad', u'-------------')
			sender.send_msg('Mammad', newPhone)
			sender.send_msg('Mammad', newName)
			sender.send_msg('Mammad', newClass)
			sender.send_msg('Mammad', u'-------------')

			# msg = Message(u"بابت ثبت نام با موفقیت انجام شد",
			# 		recipients = [newEmail],
			# 		sender = 'gli.mhmd@gmail.com',
			# 		body = u'Hello {}\n بابت ثبت نام سپاسگذاریم . به زودی از طریق تلگرام با شما تماس میگیریم'.format(newName)
			# 		)

			# admin_msg = Message ("You have a new student",
			# 		recipients = ['gli.mhmd@gmail.com'],
			# 		sender = 'gli.mhmd@gmial.com',
			# 		body = u'Your contact {} asked a question with the content \n----------\n"{}"\n----------\n, \nPlease answer through this email {}'.format(newName, newPhone, newClass)
			# 	)
			# mail.send(msg)
			# mail.send(admin_msg)
			return redirect(url_for('send_request', registeredClass = newClass))
	return render_template('register.html', form = form, error = error)


@app.route('/request/<int:registeredClass>', methods=['GET', 'POST'])
def send_request(registeredClass):
	if registeredClass == 1 or 2 or 3:
		amount = 25000
	client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
	result = client.service.PaymentRequest('111111111111111111111',
						amount,
						description,
						email,
						mobile,
						str(url_for('verify', _external=True, amount = amount)))
	if result.Status == 100:
		return redirect('https://www.zarinpal.com/pg/StartPay/' + result.Authority)
	else:
		return 'Error'



@app.route('/verify/<int:amount>', methods=['GET', 'POST'])
def verify(amount):
	amount = amount
	client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
	if request.args.get('Status') == 'OK':
		result = client.service.PaymentVerification('111111111111111111111',
							request.args['Authority'],
							amount)
		if result.Status == 100:
			return 'Transaction success. RefID: ' + str(result.RefID)
		elif result.Status == 101:
			return 'Transaction submitted : ' + str(result.Status)
		else:
			return 'Transaction failed. Status: ' + str(result.Status)
	else:
		return 'Transaction failed or canceled by user'



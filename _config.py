import os 
from datetime import timedelta


SQLALCHEMY_TRACK_MODIFICATIONS = True


basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_NAME = 'models.db'
DATABASE_PATH = os.path.join(basedir, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH


CSRF_ENABLED = True
SECRET_KEY = os.urandom(24)

RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_PARAMETERS = {'hl': 'fa'}

PERMANENT_SESSION_LIFETIME = timedelta(days=3)


#smpt config 
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'gli.mhmd@gmail.com'
MAIL_PASSWORD = 'sheE111@!'
DEFAULT_MAIL_SENDER = 'gli.mhmd@gmail.com'


#zarinpal
ZARINPAL_WEBSERVICE = 'https://www.zarinpal.com/pg/services/WebGate/wsdl'
MMERCHANT_ID = '111111111111111111111'
description = u'ثبت نام کلاس فرنچ آنلاین'
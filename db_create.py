from views import db
from models import Register, Question


db.create_all()

db.session.add(Question('mohmmad', 'asdf@asf.ss', 'salam'))

db.session.commit()
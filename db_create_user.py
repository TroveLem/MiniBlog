from project import db
from project.models import Users

db.create_all()

db.session.add(Users("Lem", "lemebay@yahoo.com", "Millpond0"))

db.session.commit()
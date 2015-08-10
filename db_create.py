from project import db
from project.models import BlogPost

db.create_all()

db.session.commit()
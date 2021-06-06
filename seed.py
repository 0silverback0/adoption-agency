from models import Pet, db 
from app import app

db.drop_all()
db.create_all()

pet_1 = Pet(name='Trixy', species='snake')

db.session.add(pet_1)
db.session.commit()
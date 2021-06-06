from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption' # create and change data base
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """ Renders Home page """

    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ displays and renders add pet form data then commits to database"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = None if form.photo_url.data == '' else form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('add-pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def display_pet_details(pet_id):
    """ displays pet details and edit page, commits changes to database"""

    form = EditPetForm()
    pet = Pet.query.get(pet_id)

    if form.validate_on_submit():
        pet.photo_url = pet.photo_url if form.photo_url.data == '' else form.photo_url.data
        pet.notes = pet.notes if form.notes.data == '' else form.notes.data
        pet.available = pet.available if form.available.data == '' else form.available.data

        db.session.commit() #no need to db.session.add since its just an update

        return redirect('/')

    else:
        return render_template('pet-details.html', pet=pet, form=form)
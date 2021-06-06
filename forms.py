from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, URL, NumberRange, Optional

class AddPetForm(FlaskForm):
    """ create add pet form """

    name = StringField('Pet name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('pine', 'Porcupine')])
    photo_url = StringField('Photo_url', validators=[Optional(), URL()]) 
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message='Age must be between 0 and 30')])
    notes = StringField('Notes')

class EditPetForm(FlaskForm):
    """ create edit pet form """
    photo_url = StringField('Photo_url', validators=[Optional(), URL(message='Invalid URL')])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available?')

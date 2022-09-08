"""Forms for Pet Adoption Agency."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, AnyOf, URL, Optional, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding new pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = FloatField("Age (in human years)", validators=[NumberRange(min=0, max=30), Optional()])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")
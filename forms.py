from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange, Length

class PetForm(FlaskForm):
    """Form for adopting pets."""

    name = StringField("Name", validators=[InputRequired(message="Pet Name can't be blank")])
    species = SelectField("Species", 
            choices=[("cat", "cat"), ("dog", "dog"), ("porcupine","porcupine")], 
            validators=[InputRequired(message="Species can't be blank")]) 
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])

class EditForm(FlaskForm):
    """Edit Form for pets."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")

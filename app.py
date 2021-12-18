"""Adoption application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'

# db = SQLAlchemy()
# db.app = app
# db.init_app(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# Add Template

@app.route('/')
def homepage():
    """Listing Pets for Adoption"""
    pets = Pet.query.all()
    return render_template('listing.html', pets=pets)

@app.route('/add', methods=['GET','POST'])
def add_pet():
    """Form to add Pets"""
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')

    else:
        return render_template('add.html', form=form)

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit_pet(id):
    """Form to edit pets"""
    pet = Pet.query.get_or_404(id)
    form = EditForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect('/')

    else:
        return render_template('edit.html', pet=pet, form=form)

    




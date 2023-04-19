"""Flask app for adopt app."""

from flask import Flask, url_for, render_template, redirect, flash, jsonify, request

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secrets"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)



# home route
@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

# create add pet route
@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        pet_name = request.form['name']
        pet_species = request.form['species']
        pet_age = request.form['age']

        pet = Pet(name=pet_name, species=pet_species, age=pet_age)
        db.session.add(pet)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_pet.html', form=form)

# run Flask app
if __name__ == '__main__':
    app.run()

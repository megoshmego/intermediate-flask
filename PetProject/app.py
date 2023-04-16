from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)



@app.route('/')
def index():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    form = PetForm()
    if form.validate_on_submit():
        pet = Pet(name=form.name.data, species=form.species.data, age=form.age.data, image_url=form.image_url.data, description=form.description.data)
        db.session.add(pet)
        db.session.commit()
        flash('Pet added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_pet.html', form=form)

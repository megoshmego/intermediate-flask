class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

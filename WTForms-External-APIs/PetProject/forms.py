from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, NumberRange

class AddPetForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    species = StringField('Species', validators=[DataRequired(), Length(min=1, max=100)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=200)])
    image = FileField('Image', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(max=500)])
    submit = SubmitField('Add Pet')

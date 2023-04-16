## WTF FORMS 

has server side validation 
adds logic for validation
adds protection from security attacks

must first establish a class "class AddSnackForm(FlaskForm)"


  ex. from flask_wtf import FlaskForm
  from wtforms import StringField, FloatField
  class AddSnackForm(FlaskForm):
    """form for adding snack"""
    
    name = StringField("Snack Name")
    price = FloatField("Price in USD")

BoolField exists

  import BooleanField
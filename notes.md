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

  example in the add_snack_form


also DateField exists, as well as DateTimeField automatically generates the type of 
form we will need, do not have to specifiy if it only accepts integers or boolean

theres also RadioField


category = RadioField("Category", choices=[('ec', 'Ice Cream'), ('chips', 'Potato Chips'), ('', 'Candy/Sweets')])

must coerce into something other than a string if needed 


Dynamic Selectors = ussed in the employees/new forms.  can use the get and post methods
the depts field uses db.sessions.query and a list which automatically creates a tuple 

  QUESTIONS - why does it create a tuple? 


can add another selection for the above with ipython 

choices dynamic is expecting tuples, and is must easier than creating various lists of acceptable input. 

validated means that if a post request, makes sure the CSRF token if valid, and makes sure some InputRequired is there, such as a name or email. it also validates where or not it is the specified form, such as if its supposed to be a string or int, etc. 

to add an error if the wrong kind of input or no input is entered, 

{{% for err in field.errors %}}
{{err}}
{{% endfor %}}

custom feedback is helpful

to edit update forms, check out edit_employee_form

##STYLING

just use bootstrap

display can easily change the size of text 

row justify-content-center is the easiest way to center rows 

bootstrap docs have some very interesting formats as well. 

### TESTING 

testing the CSRF token- must disable the CSRF or testing will not work 

app.config['WTF_CSRF_ENABLED'] = False
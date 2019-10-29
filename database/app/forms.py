from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

'''
The four classes that represent the field types in the Login Form class are imported from wtforms package.
This is due to the Flask-WTF extension not providing customized version. For each field, an object is created as a class variable in the `LoginForm` class.
Each field is given a description or label as a first argument. The validators argument is optional, but here it's used to attach validation behaviors to fields.
The `DataRequired` validators simply checks that the field is not submitted empty. There are many more types of validators available.
'''
class LoginForm(FlaskForm):
    #validator checks if the data attribute on the field is the 'true' value. A string with only whitespace is false
    #user login form which asks user to enter username and password
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me') #remember me checkbox
    submit = SubmitField('Sign In') #submit button
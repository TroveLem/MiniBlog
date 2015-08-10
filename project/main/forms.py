from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(Form):
        username = TextField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(Form):
        username = TextField('Username', validators=[DataRequired(),
                                                     Length(min=3, max=10)])

        email = TextField('Email', validators=[DataRequired(),
                                               Email(message=None),
                                               Length(min=6, max=40)])

        password = PasswordField('Password', validators=[DataRequired(),
                                                         Length(min=3, max=20)])

        confirmpassword = PasswordField('Confirm Password',
                                        validators=[DataRequired(),
                                                    EqualTo('password',
                                                            message='Passwords must match')])

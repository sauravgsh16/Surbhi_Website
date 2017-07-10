from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me Logged in')
	submit = SubmitField('Log In')

class RegistrationForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	username = StringField('Username', validators=[
		Required(), Length(1, 64), Regexp('^[a-zA-Z][a-zA-Z0-9_.]*$', 0,
										 'Username must only contain letters, '
										 'numbers, underscores or dots')])
	password = PasswordField('Password', validators=[Required(), 
		EqualTo('password2', message='Passwords must match')])
	password2 = PasswordField('Confirm Password', validators=[Required()])
	submit = SubmitField('Submit')

	# When method is defined as validata_ followed by the name of the field, 
	# the method is invoked in addition to an regularly defined validators
	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered')

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already exists, please select another username')
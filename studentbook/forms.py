from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms import SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterFormSt(FlaskForm):
    name = StringField('Name * ', validators=[DataRequired(),
                       Length(min=2, max=20)])
    rollno = StringField('Roll No * ', validators=[DataRequired(),
                         Length(min=8, max=8)])
    div = StringField('Div * ', validators=[DataRequired(),
                      Length(min=1, max=1)])
    class_st = StringField('Class * ', validators=[DataRequired(),
                           Length(min=2, max=2)])
    branch = StringField('Branch * ', validators=[DataRequired(),
                         Length(min=2, max=20)])
    mob = IntegerField('Mobile no', validators=[Length(min=10, max=13)])
    email = IntegerField('Email', validators=[Email()])
    add = StringField('Address', validators=[Length(min=2, max=30)])
    username = StringField('Username * ', validators=[DataRequired(),
                           Length(min=2, max=20)])
    password = PasswordField('Password * ', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password * ',
                                 validators=[DataRequired(),
                                             EqualTo('password')])
    submit = SubmitField('Sign Up')


class RegisterFormte(FlaskForm):
    name = StringField('Name *', validators=[DataRequired(),
                                             Length(min=2, max=20)])
    id_no = StringField('Id No * ', validators=[DataRequired(),
                                                Length(min=8, max=8)])
    branch = StringField('Allocated Branch * ',
                         validators=[DataRequired(), Length(min=2, max=20)])
    qualification = StringField('Qualification * ',
                                validators=[DataRequired(),
                                            Length(min=2, max=10)])
    mob = IntegerField('Mobile no', validators=[Length(min=10, max=13)])
    email = IntegerField('Email', validators=[Email()])
    add = StringField('Address', validators=[Length(min=2, max=30)])
    username = StringField('Username * ',
                           validators=[DataRequired(),
                                       Length(min=2, max=20)])
    password = PasswordField('Password * ', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password * ',
                                 validators=[DataRequired(),
                                             EqualTo('password')])
    submit = SubmitField('Sign Up')


class RegisterFormco(FlaskForm):
    name = StringField('Name * ', validators=[DataRequired(),
                                              Length(min=2, max=20)])
    rollno = StringField('Roll No * ', validators=[DataRequired(),
                                                   Length(min=8, max=8)])
    position = StringField('Position in Committee * ',
                           validators=[DataRequired(),
                                       Length(min=2, max=10)])
    committee = StringField('Name of the Committee * ',
                            validators=[DataRequired(), Length(min=2, max=10)])
    class_co = StringField('Class * ', validators=[DataRequired(),
                                                   Length(min=2, max=2)])
    branch = StringField('Branch * ', validators=[DataRequired(),
                                                  Length(min=2, max=20)])
    mob = IntegerField('Mobile no', validators=[Length(min=10, max=13)])
    email = IntegerField('Email', validators=[Email()])
    add = StringField('Address', validators=[Length(min=2, max=30)])
    username = StringField('Username * ', validators=[DataRequired(),
                                                      Length(min=2, max=20)])
    password = PasswordField('Password * ', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password * ',
                                 validators=[DataRequired(),
                                             EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    user_type = SelectField('Login As',
                            validators=[DataRequired()],
                            choices=[('st', 'Student'),
                                     ('te', 'Teacher'),
                                     ('co', 'Committee Member')])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

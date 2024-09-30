from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class StudentForm(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired()])
    group = StringField('Group', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    grade = FloatField('Grade', validators=[DataRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField('Save')

class SearchForm(FlaskForm):
    search = StringField('Search')
    submit = SubmitField('Search')
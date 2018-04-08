from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea

class MyForm(FlaskForm):
    name = TextAreaField('Your Text Below', validators=[DataRequired(), Length(max=1000000)], widget=TextArea())
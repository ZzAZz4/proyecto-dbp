from flask_wtf import FlaskForm
from werkzeug.datastructures import Range
from wtforms import StringField, PasswordField, FloatField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    pass
    #name = StringField('Name',validators=[DataRequired(), Length(min=3, max=25)])
    #username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    #password = PasswordField('Password',validators=[DataRequired(), Length(min=10, max=25)])


class ProductForm(FlaskForm):
    pass
    #nombre = StringField('nombre', validators=[DataRequired(), Length(min=5, max=40)])
    #descripcion = StringField('descripcion', validators=[DataRequired(), Length(min=3, max=25)])
    #url = [DataRequired(), URL(message='Must be a valid URL')]
    #precio = FloatField('precio',validators=[DataRequired(), Range(3.0,25.0)] )


class CreateProductForm(FlaskForm):
    pass
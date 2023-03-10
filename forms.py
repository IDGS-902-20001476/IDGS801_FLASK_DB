from wtforms import Form 
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre')
    apellidos=StringField('apellidos')
    email=EmailField('correo')

class UserForm2(Form):
    id=IntegerField('id')
    nombreM=StringField('nombre')
    apellidosM=StringField('apellidos')
    emailM=EmailField('correo')
    especialidad=StringField('especialidad')
    turno=StringField('turno')
    


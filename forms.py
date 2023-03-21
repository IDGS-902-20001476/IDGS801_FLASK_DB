from wtforms import Form 
from wtforms import StringField, IntegerField, SelectField, RadioField,SubmitField
from wtforms import EmailField
from wtforms import validators
from flask_wtf import FlaskForm
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
class ResistenciaGuardar(Form):
    cl=StringField('cl')
    b1=StringField('b1')

class ResistenciaForm(FlaskForm):
    colors = [('','Selecciona'),("negro", "Negro"), ("marron", "Marrón"), ("rojo", "Rojo"), ("naranja", "Naranja"),
                      ("amarillo", "Amarillo"), ("verde", "Verde"), ("azul", "Azul"), ("violeta", "Violeta"),
                      ("gris", "Gris"), ("blanco", "Blanco")]
    banda1 = SelectField('Primera Banda', choices=colors, validators=[validators.InputRequired('Elija una opción')])
    banda2 = SelectField('Segunda Banda', choices=colors, validators=[validators.InputRequired('Elija una opción')])
    banda3 = SelectField('Tercera Banda (Multiplicador)', choices=[('','Selecciona'),('negro', 'Negro x1 Ω'), ('marron', 'Marron x10 Ω'), 
                                              ('rojo', 'Rojo x100 Ω'), ('naranja', 'Naranja x1 kΩ'),
                                              ('amarillo', 'Amarillo x10 kΩ'), ('verde', 'Verde x100 kΩ'), 
                                              ('azul', 'Azul x1 MΩ'), ('violeta', 'Violeta x10 MΩ'),
                                              ('gris', 'Gris x100 MΩ'), ('blanco', 'Blanco x10 GΩ')],
                                                       validators=[validators.InputRequired('Elija una opción correcta')])
    tolerancia = RadioField('Tolerancia', choices=[('oro', 'ORO ± 5%'), ('plata', 'PLATA ± 10%')], 
                           validators=[validators.InputRequired(message='Este campo no puede quedarse vacio')])
    calcular = SubmitField("Calcular")
    leer = SubmitField("Leer")



from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos
import forms

alumnos= Blueprint('alumnos', __name__)

@alumnos.route("/", methods=['GET', 'POST'])
def index():
    create_form=forms.UserForm(request.form)
    if request.method=='POST':
        alum=Alumnos(nombre=create_form.nombre.data,
                     apellidos=create_form.apellidos.data,
                     email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
    return render_template('index.html', form=create_form)

@alumnos.route("/ABCompleto", methods=['GET', 'POST'])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    #select * from alumnos
    alumnos=Alumnos.query.all()
    return render_template('ABCompleto.html', form=create_form, alumnos=alumnos)

@alumnos.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form= forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #select * from alumnos where id==id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email

    
    if request.method=='POST':
        id=create_form.id.data
        #select * from alumnos where id==id
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        
        alum.nombre=create_form.nombre.data
        alum.apellidos=create_form.apellidos.data
        alum.email=create_form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    
    return render_template('modificar.html', form=create_form)

@alumnos.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form= forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #select * from alumnos where id==id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email

    if request.method=='POST':
        id=create_form.id.data
        #select * from alumnos where id==id
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        
        alum.nombre=create_form.nombre.data
        alum.apellidos=create_form.apellidos.data
        alum.email=create_form.email.data
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    
    return render_template('eliminar.html', form=create_form)
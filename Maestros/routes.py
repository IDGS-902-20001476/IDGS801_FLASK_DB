from flask import Blueprint, render_template, redirect, url_for, request, flash
from db import get_connection
from models import db
from models import Maestros
import forms

maestros= Blueprint('maestros', __name__)


@maestros.route("/insertarMaestro",methods=['GET', 'POST'])
def index():
    create_form=forms.UserForm2(request.form)
    if request.method == 'POST':
        nombreM = create_form.nombreM.data
        apellidosM = create_form.apellidosM.data
        emailM = create_form.emailM.data
        especialidad = create_form.especialidad.data
        turno = create_form.turno.data
        try:
           connection=get_connection()
           with connection.cursor() as cursor:
                cursor.execute('call agrega_maestro(%s,%s,%s,%s,%s)', (nombreM, apellidosM, emailM, especialidad, turno))
           connection.commit()
           connection.close()

        except Exception as ex:
            print('ERROR {}'.format(ex))

        return redirect(url_for('maestros.ABCompleto'))
    
    return render_template('maestro.html',form=create_form)
    

@maestros.route("/modificarMaestro",methods=['GET','POST'])
def modificar():
    create_fprm=forms.UserForm2(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        connection = get_connection()
        try:
           with connection.cursor() as cursor:
               cursor.execute('CALL consulta_maestrp(%s)',(id))
               resultset = cursor.fetchall()
           create_fprm.id.data=request.args.get('id')
           create_fprm.nombreM.data=resultset[0][1]
           create_fprm.apellidosM.data=resultset[0][2]
           create_fprm.emailM.data=resultset[0][3]
           create_fprm.especialidad.data=resultset[0][4]        
           create_fprm.turno.data=resultset [0][5]   
        except Exception as ex:
           print(ex)
        finally:
           connection.close()

    if request.method=='POST':
        id=create_fprm.id.data
        nombreM = create_fprm.nombreM.data
        apellidosM = create_fprm.apellidosM.data
        emailM = create_fprm.emailM.data
        especialidad = create_fprm.especialidad.data
        turno =create_fprm.turno.data
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('CALL modificar_maestro(%s,%s,%s,%s,%s,%s)', (id, nombreM, apellidosM, emailM, especialidad, turno))
            connection.commit()
            connection.close()

        except Exception as ex:
           print('ERROR {}'.format(ex))
        return redirect(url_for('maestros.ABCompleto'))
    return render_template('modificarMaestro.html', form= create_fprm)


@maestros.route("/eliminarMaestro",methods=['GET','POST'])
def eliminar():
    create_fprm=forms.UserForm2(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        connection = get_connection()
        try:
           with connection.cursor() as cursor:
               cursor.execute('CALL consulta_maestrp(%s)',(id))
               resultset = cursor.fetchall()
           create_fprm.id.data=request.args.get('id')
           create_fprm.nombreM.data=resultset[0][1]
           create_fprm.apellidosM.data=resultset[0][2]
           create_fprm.emailM.data=resultset[0][3]
           create_fprm.especialidad.data=resultset[0][4]          
           create_fprm.turno.data=resultset [0][5] 
        except Exception as ex:
           print(ex)
        finally:
           connection.close()
    if request.method=='POST':
        id=create_fprm.id.data
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('CALL eliminar_maestro(%s)', (id))
            connection.commit()
            connection.close()

        except Exception as ex:
           print('ERROR {}'.format(ex))
        return redirect(url_for('maestros.ABCompleto'))
    return render_template('eliminarMaestro.html', form= create_fprm)


@maestros.route("/ABCompletoMaestro",methods=["GET","POST"])
def ABCompleto():
    create_form=forms.UserForm2(request.form)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute('call consulta_maestros()')
            resultset = cursor.fetchall()
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
    print (resultset)
    return render_template("ABCompletoMaestro.html", form=create_form, resultset=resultset)

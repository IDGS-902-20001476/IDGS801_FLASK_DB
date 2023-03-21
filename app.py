
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms
from flask_wtf import CSRFProtect
from collections import Counter
from actResistencia import resistencia
from flask import jsonify, flash, Response, make_response
#from config import DevelopmentConfig
#from flask_wtf.csrf import CSRFProtect
#from models  import db
import math


app=Flask(__name__)
#app.config.from_object(DevelopmentConfig)

app.config['SECRET_KEY']="esta es tu clave encriptada"
app.config.from_object(resistencia)
#csrf=CSRFProtect()

"""
@app.route("/", methods=['GET', 'POST'])
def index():
    create_form=forms.UserForm(request.form)
    if request.method=='POST':
        alum=Alumnos(nombre=create_form.nombre.data,
                     apellidos=create_form.apellidos.data,
                     email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
    return render_template('index.html', form=create_form)

@app.route("/ABCompleto", methods=['GET', 'POST'])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    #select * from alumnos
    alumnos=Alumnos.query.all()
    return render_template('ABCompleto.html', form=create_form, alumnos=alumnos)

@app.route("/modificar", methods=['GET', 'POST'])
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

@app.route("/eliminar", methods=['GET', 'POST'])
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

@app.route("/maestros", methods=['GET', 'POST'])
def maestros():
    create_form=forms.UserForm2(request.form)
    if request.method=='POST':
        mae=Maestros(nombreM=create_form.nombreM.data,
                    apellidosM=create_form.apellidosM.data,
                    emailM=create_form.emailM.data,
                    especialidad= create_form.especialidad.data,
                    turno=create_form.turno.data)
        db.session.add(mae)
        db.session.commit()
    return render_template('maestro.html', form=create_form)

@app.route("/ABCompletoMaestros", methods=['GET', 'POST'])
def ABCompletoMaestros():
    create_form = forms.UserForm(request.form)
    #select * from alumnos
    maestros=Maestros.query.all()
    return render_template('ABCompletoMaestro.html', form=create_form, maestros=maestros)
"""
@app.route("/TraductorR", methods=["GET","POST"])
def traductorR():
    reg_traductor = forms.TraductorForm(request.form)
    if request.method=='POST':
        selTrad= (request.form.get("btnTraductor"))
        palabraT=str(reg_traductor.txtPalabra.data).lower()
        if(palabraT==""):
            ree="Debes ingresar la palabra a traducir"
            return render_template("TraductorR.html",form=reg_traductor, ree=ree)
        else:
            f=open('Traductor.txt', 'r')
            txtP = [linea.rstrip('\n') for linea in f]
            if(selTrad=="1"):
                for i in range(len(txtP)):
                    if(txtP[i-1]== (palabraT)):
                        textoE = txtP[i - 2]
                        s="La traduccion al español es: "+textoE.capitalize()
                        return render_template("TraductorR.html",s=s,form=reg_traductor)
                    else:
                        s="Lo sentimos esta palabra no fue encontrada: "+palabraT
                        return render_template("TraductorR.html",s=s,form=reg_traductor)
            elif(selTrad=="2"):
                for i in range(len(txtP)):
                    if(txtP[i-2] == palabraT):
                        textoE = txtP[i - 1]
                        s="La traduccion al ingles es: "+textoE.capitalize()
                        return render_template("TraductorR.html",s=s,form=reg_traductor)
                    else:
                        s="Lo sentimos esta palabra no fue encontrada: "+palabraT
                        return render_template("TraductorR.html",s=s,form=reg_traductor)
            else:
                r="Debes seleccionar el idioma a traducir"
                return render_template("TraductorR.html",form=reg_traductor, r=r)


    return render_template("TraductorR.html",form=reg_traductor)

def calcular_resistencia(banda1, banda2, banda3, tolerancia):

    valores = {
        "negro": 0,
        "marron": 1,
        "rojo": 2,
        "naranja": 3,
        "amarillo": 4,
        "verde": 5,
        "azul": 6,
        "violeta": 7,
        "gris": 8,
        "blanco": 9
    }
    english_names = {
        "negro": "black",
        "marron": "brown",
        "rojo": "red",
        "naranja": "orange",
        "amarillo": "yellow",
        "verde": "green",
        "azul": "blue",
        "violeta": "violet",
        "gris": "gray",
        "blanco": "white",
        "oro": "gold",
        "plata": "silver"
    }
    banda1_en = english_names[banda1]
    banda2_en = english_names[banda2]
    banda3_en = english_names[banda3]
    tolerancia_en = english_names[tolerancia]

    valor1 = valores[banda1]
    valor2 = valores[banda2]
    multiplicador = math.pow(10, valores[banda3])
    tolerancia_valor = 0.05 if tolerancia == "oro" else 0.1

    valor = (valor1 * 10 + valor2) * multiplicador
    valor_minimo = valor * (1 - tolerancia_valor)
    valor_maximo = valor * (1 + tolerancia_valor)

    return {
        "colorBanda1": banda1_en,
        "colorBanda2": banda2_en,
        "colorBanda3": banda3_en,
        "colorTolerancia": tolerancia_en,
        "banda1": banda1,
        "banda2": banda2,
        "banda3": banda3,
        "tolerancia": tolerancia,
        "valor": valor,
        "valor_minimo": valor_minimo,
        "valor_maximo": valor_maximo
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.ResistenciaForm(request.form)
    resultados_guardados = []

    with open("resistencia.txt", "r") as f:
        valores_guardados = [line.strip().split(",") for line in f]
        
        for valores in valores_guardados:
            if len(valores) == 4:
                resultado_guardado = calcular_resistencia(*valores)
                resultados_guardados.append(resultado_guardado)

    if request.method == 'POST': 
        if request.form.get('leer'):
            banda1 = request.form['banda1']
            banda2 = request.form['banda2']
            banda3 = request.form['banda3']
            if 'tolerancia' in request.form and request.form['tolerancia']:
                      tolerancia = request.form['tolerancia']
            else:
                 tolerancia = None
            print (tolerancia)
            if banda1=="" and banda2=="" and banda3=="" and tolerancia is None:
               return render_template('resistencias.html', form=form, valores_guardados=resultados_guardados)
            
            resultado = calcular_resistencia(banda1, banda2, banda3, tolerancia)
            valores_guardados = resultados_guardados + [resultado]

            return render_template('resistencias.html', resultado=resultado, form=form, valores_guardados=valores_guardados)

        elif request.form.get('registrar'):
            banda1 = request.form['banda1']
            banda2 = request.form['banda2']
            banda3 = request.form['banda3']
            tolerancia = request.form['tolerancia']

            with open("Resistencia.txt", "a") as f:
                f.write(",".join([banda1, banda2, banda3, tolerancia]) + "\n")

            return render_template('resistencias.html', form=form, resultados_guardados=resultados_guardados)

    return render_template('resistencias.html', form=form, resultados_guardados=resultados_guardados)




if __name__ == "__main__":
    #csrf.init_app(app)
    app.run(debug=True,port=3000)

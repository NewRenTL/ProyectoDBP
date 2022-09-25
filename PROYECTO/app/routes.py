#Desde app importo app
from app import app
#Desde datetime importo datetime
from datetime import datetime
#Importo el paquete Re
import re
#Desde flask importo render_template(plantilla de renderizado) y request(solicitud[MetodoFlask])
from flask import render_template,request
from app import db
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    args = request.args
    #user = {'username':'Diego'}
    user1 = args.get('user')
    print(type(user1))
    if (user1 != None and len(user1) != 0):
        print(user1) 
        user = {'username':str(user1)}
    else:
        user = {'username':'Desconocido'}
   
    #El resultado de la funcio nsera un render_template o una 
    #plantilla htmlm y luego le puedo colocar parametros
    return render_template('index.html',title='Home',user = user)    

#Cuando colocamos "<parametro>" puedes pasar un valor en ruta
@app.route('/hello/<name>')
def hello_there(name):
    #El Valor colocado en la ruta en este caso <name> sera pasado como parametro
    #dentro de la funcion y luego esta puede ser usado posteriormente


    #Datetime.now() me devuelve la fecha y hora actual
    now = datetime.now()
    formatted_now = now.strftime('%A, %d %B, %Y at %X')
    
    #Estás diciéndole a la función que considere todos los caracteres que se encuentren en el abecedario tanto en minúscula como mayúscula
    #También se le conoce como una expresión regular en donde a partir de una cadena verificará si dicho carácter se encuentra dentro del conjunto del abecedario:
    #Por ejemplo: [a-zA-Z]+ significa que la función se llevará a cabo para todas las cadenas en las que cada carácter pertenezca al abecedario ya sea de minúsculas o
    #  mayúsculas. Cabe resaltar que el “+” permite que puedas armar una cadena vacía o con la longitud a tu preferencia

    #Ejemplo en este caso estoy usando el parametro name de la ruta
    match_object = re.match("[a-zA-Z]+",name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
    
    content = "Hola de nuevo, " + clean_name + " Esta es la fecha de hoy "+formatted_now;
    return content    

#Este sera del metodo Get para poder obtener parametros de la URL O ruta
#Por eso colocoamos methods = ['GET']
@app.route("/add/user",methods=["GET"])
def addUser():
    #Solicito argumentos
    args = request.args
    #Solicito datos para username,password y email
    username = args.get('username')
    password = args.get('password')
    email = args.get('email')

    newUser = User(username = username, password = password, email = email)
    try:
        db.session.add(newUser)
        db.session.commit()
        return "El usuario fue añadido con exito"
    except Exception as error:
        return "Ups hubo un error al subir al usuario {} ".format(error)


#Ruta addNumbers para agregar numeros
@app.route('/addNumbers',methods=['GET'])
def add():
    args = request.args
    val1 = int(args.get("val1"))
    val2 = int(args.get("val2"))
    return str(val1 + val2)


@app.route("/users")
def  getAllUsers():
    users = User.query.all()
    userStrings = ""

    #<br> es un salto de linea en el texto
    for user in users:
        userStrings += user.username + " " + user.password + " " + user.email + "<br>"
    return userStrings;




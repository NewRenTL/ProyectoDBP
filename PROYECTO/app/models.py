from datetime import datetime
import re

from app import db

class Comidas(db.Model):
    #Creo una columna NombreComida donde iran los nombres de las comidas junto con su contador
    NombreComida = db.Column(db.String(80),primary_key=True)
    contador = db.Column(db.Integer,default=0)
    def __repr__(self):
        return '<Comida:{} Contador:{}'.format(self.NombreComida,self.Contador)

class User(db.Model):

    #Creo la columna ID que es entera, sera mi llave primaria y se ira 
    #autoincrementando por si misma
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)


    #Creo la columna username que sera de tipo String que guarde
    # 64 caracteres como maximo, y que sea Unico (unique)
    username = db.Column(db.String(64),index = True, unique = True)


    #Creo la columna email que sera de tipo String que guarde
    # 120 caracteres como maximo, y que sea Unico (unique)
    email = db.Column(db.String(120),index = True, unique = True)


    #Creo la columna password que guardara la contraseña , puede 
    #guardar como maximo 128 caracteres 
    password = db.Column(db.String(128))
    
    def __repr__(self):
        #Este retornara un string el cual entre esos parentesis gracias al 
        # format , se guarda el username, y podre imprimirlo
        return'<User {}>'.format(self.username)

#DB.create_all() me permitira crear las tablas dentro de mi base de datos
#Nota:No sobreescribe la tabla
db.create_all()
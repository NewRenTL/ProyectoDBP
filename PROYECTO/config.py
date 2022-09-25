import os

#De aqui sacamos directamentel a base de Datos
basedir = os.path.join(os.path.dirname(__file__))


##Condiguracion
class Config(object):
    #La url de la base de datos funciona asi:
    # 'nombredebasededatos://user:contraseña@localhost:puerto/namedatabase'
    
    #¿Por que tenemos un Or? 
    #Por lo gneeral lo hacemos para evitar que se exhiba los datos 
    #de mi base de datos , por que puedo mostrar informacion y es 
    # peligroso
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')or \
        'postgresql://postgres:960365560@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
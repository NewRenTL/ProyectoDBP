from tkinter.tix import INTEGER
import psycopg2
from psycopg2 import Error


try:
    #Conexion a la base de datos existente
    connection = psycopg2.connect(user = "postgres",password ="960365560",database = "postgres", host = "localhost",port ="5432")

    #Creo un cursor que me permitira realizar operaciones en 
    #la base de datos

    cursor = connection.cursor()

    #Imprimo los detalles del server PSQL
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(),"\n");
    # Ejecuto u nSQL Query para ver la version SQL
    cursor.execute("SELECT version()")
    # Obtengo el resultado
    record = cursor.fetchone()

    print("You are connected to - ",record,"\n")
    #connection.commit();
    ##Captura una sola fila
    ##record = cursor.fetchone()
    ##Captura todas las filas 
    #record = cursor.fetchall()  ;

    #print(record)

except (Exception,Error) as error:
    print("Error while connecting to PostgreSQL",error)

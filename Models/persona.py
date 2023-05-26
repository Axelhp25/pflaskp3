import conexion

class modelPersona():
    @classmethod
    def create(self, db,nombre,apellido,tel,correo):
        try:
            cursor = db.cursor()
            query = "INSERT INTO personas(nombre,apellido,numero,correoElectronico) VALUES('{}','{}','{}','{}')".format(nombre,apellido,tel,correo)
            cursor.execute(query)
            db.commit()
            return 'registro insertado!'
        except Exception as ex:
            raise Exception(ex)
        
    def ver(db):
        try:
            cursor = db.cursor()
            query = "select nombre,apellido,numero,correoElectronico from personas"
            cursor.execute(query)
            lista=[]
            for i in cursor:
                lista.append(i)
            return lista
        except Exception as ex:
            raise Exception(ex)